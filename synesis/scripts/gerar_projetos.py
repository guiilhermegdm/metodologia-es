#!/usr/bin/env python3
"""Gera e compila os projetos Synesis do mapeamento sistemático.

Fluxo automatizado:
  1. Lê os .bib coletados (bases indexadas + outras fontes) em ../estudos-primarios-coletados
  2. Deduplica automaticamente os registros das bases (mesmo DOI ou mesmo título)
  3. Cria/atualiza a planilha de triagem das bases (triagem-bases.csv), preservando
     as decisões já preenchidas pela equipe
  4. Gera o projeto Synesis de SELEÇÃO (um SOURCE por registro, um ITEM por decisão)
  5. Gera o projeto Synesis de EXTRAÇÃO (um SOURCE + ITEM por estudo incluído)
  6. Compila os dois projetos com o compilador Synesis (CSV + Excel + JSON)

Uso (a partir da pasta synesis/):
    pip install -r requirements.txt
    python scripts/gerar_projetos.py
    python scripts/relatorio.py
"""
import csv
import re
import shutil
import subprocess
import sys
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]          # raiz do repositório
SYN = RAIZ / "synesis"
COLETA = RAIZ / "estudos-primarios-coletados"
DADOS = RAIZ / "dados"

BASES = {
    "ieee_xplore": COLETA / "bases-indexadas" / "ieee-xplore.bib",
    "acm_dl": COLETA / "bases-indexadas" / "acm-digital-library.bib",
}
OUTRAS = [COLETA / "outras-fontes" / "candidatos-avaliados.bib",
          COLETA / "outras-fontes" / "candidatos-sem-metadados.bib"]
SELECAO_CSV = COLETA / "selecao-estudos.csv"        # decisões da elegibilidade (outras fontes)
TRIAGEM_CSV = COLETA / "triagem-bases.csv"          # decisões da triagem (bases indexadas)
EXTRACAO_CSV = DADOS / "extracao-estudos-incluidos.csv"


# ----------------------------------------------------------------- utilidades
def ler_bib(caminho):
    """Retorna lista de dicts {chave, tipo, title, year, doi} na ordem do arquivo."""
    texto = caminho.read_text(encoding="utf-8")
    regs = []
    for m in re.finditer(r"^@(\w+)\{([^,\s]+),(.*?)(?=^@|\Z)", texto, re.S | re.M):
        corpo = m.group(3)

        def campo(nome):
            # valor entre chaves, admitindo um nível de chaves internas (ex.: {Título com {Sigla}})
            mm = re.search(r"\b" + nome + r"\s*=\s*\{((?:[^{}]|\{[^{}]*\})*)\}", corpo, re.I)
            return re.sub(r"\s+", " ", mm.group(1)).strip() if mm else ""
        regs.append({"chave": m.group(2), "tipo": m.group(1).lower(),
                     "title": campo("title"), "year": campo("year"), "doi": campo("doi").lower()})
    return regs


def normaliza_titulo(t):
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]", "", t)


def limpa(valor):
    """Valores de uma linha, sem caracteres que a sintaxe Synesis interpreta."""
    return re.sub(r"\s+", " ", str(valor)).replace("#", "nº").strip()


def ler_csv(caminho):
    with open(caminho, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


# ----------------------------------------------------------------- seleção
def gerar_selecao():
    pasta = SYN / "selecao"
    (pasta / "bib").mkdir(parents=True, exist_ok=True)

    # registros de outras fontes (já avaliados na elegibilidade)
    decisoes_outras = {r["chave_bibtex"]: r for r in ler_csv(SELECAO_CSV)}
    outras = []
    for b in OUTRAS:
        shutil.copy(b, pasta / "bib" / b.name)
        outras += ler_bib(b)

    vistos_doi = {r["doi"]: r["chave"] for r in outras if r["doi"]}
    vistos_tit = {normaliza_titulo(r["title"]): r["chave"] for r in outras if r["title"]}

    # registros das bases, com deduplicação automática
    base_regs = []
    for base, bib in BASES.items():
        shutil.copy(bib, pasta / "bib" / bib.name)
        for r in ler_bib(bib):
            dup = None
            tn = normaliza_titulo(r["title"])
            if r["doi"] and r["doi"] in vistos_doi:
                dup = vistos_doi[r["doi"]]
            elif tn and len(tn) > 30 and tn in vistos_tit:
                dup = vistos_tit[tn]
            if r["doi"]:
                vistos_doi.setdefault(r["doi"], r["chave"])
            if tn:
                vistos_tit.setdefault(tn, r["chave"])
            base_regs.append(dict(r, base=base, duplicata_de=dup))

    # planilha de triagem das bases: cria ou preserva decisões já preenchidas
    anteriores = {r["chave_bibtex"]: r for r in ler_csv(TRIAGEM_CSV)} if TRIAGEM_CSV.exists() else {}
    campos = ["chave_bibtex", "base", "ano", "titulo", "doi", "duplicata_de", "decisao", "criterio", "justificativa"]
    linhas = []
    for r in base_regs:
        ant = anteriores.get(r["chave"], {})
        if r["duplicata_de"]:
            dec, crit, just = "duplicata", "DUP", f"Mesmo DOI/título de {r['duplicata_de']}"
        else:
            dec = ant.get("decisao") or "pendente"
            crit = ant.get("criterio") or "nao_aplicado"
            just = ant.get("justificativa", "")
        linhas.append({"chave_bibtex": r["chave"], "base": r["base"], "ano": r["year"], "titulo": r["title"],
                       "doi": r["doi"], "duplicata_de": r["duplicata_de"] or "", "decisao": dec,
                       "criterio": crit, "justificativa": just})
    with open(TRIAGEM_CSV, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=campos)
        w.writeheader()
        w.writerows(linhas)

    # anotações Synesis
    etapa_de = {"pendente": 1, "duplicata": 2}  # índices do campo ORDERED etapa
    out = ["# Gerado automaticamente por scripts/gerar_projetos.py — não editar à mão.",
           "# Para registrar decisões, edite estudos-primarios-coletados/triagem-bases.csv e rode o script de novo.", ""]
    for l in linhas:
        out += [f"SOURCE @{l['chave_bibtex']}", f"    base: {l['base']}"]
        if l["duplicata_de"]:
            out.append(f"    duplicata_de: {l['duplicata_de']}")
        out += ["END SOURCE", "", f"ITEM @{l['chave_bibtex']}",
                f"    etapa: {etapa_de.get(l['decisao'], 3)}",
                f"    decisao: {l['decisao']}", f"    criterio: {l['criterio']}"]
        if l["justificativa"]:
            out.append(f"    justificativa: {limpa(l['justificativa'])}")
        out += ["END ITEM", ""]
    for r in outras:
        d = decisoes_outras[r["chave"]]
        crit = "CI" if d["decisao"] == "incluído" else d["criterio"]
        dec = "incluido" if d["decisao"] == "incluído" else "excluido"
        out += [f"SOURCE @{r['chave']}", "    base: outras_fontes", "END SOURCE", "",
                f"ITEM @{r['chave']}", "    etapa: 4", f"    decisao: {dec}", f"    criterio: {crit}"]
        if d.get("justificativa"):
            out.append(f"    justificativa: {limpa(d['justificativa'])}")
        out += ["END ITEM", ""]
    (pasta / "registros.syn").write_text("\n".join(out), encoding="utf-8")

    bibs = "\n".join(f'    INCLUDE BIBLIOGRAPHY "bib/{p.name}"' for p in list(BASES.values()) + OUTRAS)
    (pasta / "selecao.synp").write_text(f"""PROJECT selecao_mapeamento_agentes_multimodais
    TEMPLATE "selecao.synt"
{bibs}
    INCLUDE ANNOTATIONS "registros.syn"
    METADATA
        version: 1.0
        dataset: Registros das strings de busca (IEEE Xplore, ACM DL) e de outras fontes
    END METADATA
END PROJECT
""", encoding="utf-8")
    return len(base_regs), len(outras)


# ----------------------------------------------------------------- extração
POP = {"TEA": "TEA", "TDAH": "TDAH", "Dislexia": "Dislexia", "DI": "DI", "Surdez": "Surdez", "Misto": "Misto"}
AGENTE = {"Robô social": "robo_social", "RV/avatar": "rv_avatar", "STI": "sti", "Jogo sério": "jogo_serio",
          "Agente virtual": "agente_virtual", "Chatbot/LLM": "chatbot_llm", "Sistema adaptativo": "sistema_adaptativo"}
TECNICA = {"Regras/limiares": "regras_limiares", "ML clássico": "ml_classico", "Deep learning": "deep_learning",
           "DL + LLM": "dl_llm", "n.i.": "nao_informado"}
FUSAO = {"Unimodal": "unimodal", "Atributos": "atributos", "Decisão": "decisao", "Híbrida": "hibrida", "n.i.": "nao_informado"}
TEMPO = {"Sim": "sim", "Não": "nao", "n.i.": "nao_informado"}
AVAL = {"Prova de conceito": 1, "Laboratório": 2, "Experimento": 3, "Campo": 4}  # índices do campo ORDERED avaliacao
MOD = {"Texto": "mod_texto", "Voz/prosódia": "mod_voz", "Expressão facial": "mod_face", "Olhar": "mod_olhar",
       "Fisiológico/EEG": "mod_fisiologico", "Postura/gestos": "mod_postura_gestos", "Interação/logs": "mod_interacao_logs"}
EST = {"engajamento": "est_engajamento", "atenção": "est_atencao", "frustração": "est_frustracao", "tédio": "est_tedio",
       "ansiedade": "est_ansiedade", "carga cognitiva": "est_carga_cognitiva", "confusão": "est_confusao",
       "emoções básicas": "est_emocoes_basicas", "valência/ativação": "est_valencia_ativacao", "prazer": "est_prazer",
       "inatividade": "est_inatividade", "confiança": "est_confianca", "interesse": "est_interesse"}
ADP = {"Ritmo/pausas": "adp_ritmo", "Formato/modalidade": "adp_formato", "Tom/feedback afetivo": "adp_tom_feedback",
       "Dificuldade/conteúdo": "adp_dificuldade", "Regulação emocional": "adp_regulacao_emocional",
       "Apenas detecção": "adp_apenas_deteccao"}


def lista(valor, mapa):
    return ", ".join(mapa[v.strip()] for v in valor.split(";") if v.strip())


def gerar_extracao():
    pasta = SYN / "extracao"
    (pasta / "bib").mkdir(parents=True, exist_ok=True)
    shutil.copy(COLETA / "estudos-incluidos.bib", pasta / "bib" / "estudos-incluidos.bib")
    out = ["# Gerado automaticamente por scripts/gerar_projetos.py a partir de dados/extracao-estudos-incluidos.csv", ""]
    linhas = ler_csv(EXTRACAO_CSV)
    for r in linhas:
        k = r["chave_bibtex"]
        out += [f"SOURCE @{k}",
                f"    id_estudo: {r['id']}",
                f"    populacao: {POP[r['populacao']]}",
                f"    tipo_agente: {AGENTE[r['tipo_agente']]}",
                f"    tecnica: {TECNICA[r['tecnica_inferencia']]}",
                f"    fusao: {FUSAO[r['nivel_fusao']]}",
                f"    tempo_real: {TEMPO[r['tempo_real']]}",
                f"    avaliacao: {AVAL[r['tipo_avaliacao']]}",
                f"    n_participantes: {limpa(r['n_participantes'])}",
                "END SOURCE", "",
                f"ITEM @{k}",
                f"    sintese: {limpa(r['sintese'])}",
                f"    desfecho_afetivo: {limpa(r['desfecho_afetivo'])}",
                f"    modalidade: {lista(r['modalidades'], MOD)}",
                f"    estado: {lista(r['estados_inferidos'], EST)}",
                f"    adaptacao: {lista(r['estrategias_adaptacao'], ADP)}",
                "END ITEM", ""]
    (pasta / "estudos.syn").write_text("\n".join(out), encoding="utf-8")
    (pasta / "extracao.synp").write_text("""PROJECT extracao_mapeamento_agentes_multimodais
    TEMPLATE "extracao.synt"
    INCLUDE BIBLIOGRAPHY "bib/estudos-incluidos.bib"
    INCLUDE ANNOTATIONS "estudos.syn"
    INCLUDE ONTOLOGY "ontologia.syno"
    METADATA
        version: 1.0
        dataset: Estudos primários incluídos (S01-S25)
    END METADATA
END PROJECT
""", encoding="utf-8")
    return len(linhas)


# ----------------------------------------------------------------- compilação
def compilar(nome):
    pasta = SYN / nome
    saida = SYN / "saida" / nome
    if saida.exists():
        shutil.rmtree(saida)
    saida.mkdir(parents=True)
    cmd = ["synesis", "compile", f"{nome}.synp", "--strict",
           "--csv", str(saida), "--xls", str(saida / f"{nome}.xlsx"), "--json", str(saida / f"{nome}.json"), "--stats"]
    res = subprocess.run(cmd, cwd=pasta, capture_output=True, text=True)
    print(res.stdout[-1500:], res.stderr[-1500:])
    if res.returncode != 0:
        sys.exit(f"Falha ao compilar o projeto {nome}")
    relativizar(saida)


def relativizar(saida):
    """Troca os caminhos absolutos da máquina local por caminhos relativos à pasta synesis/."""
    prefixo = str(SYN) + "/"
    for arq in list(saida.glob("*.csv")) + list(saida.glob("*.json")):
        arq.write_text(arq.read_text(encoding="utf-8").replace(prefixo, ""), encoding="utf-8")
    try:
        import openpyxl
    except ImportError:
        return
    for arq in saida.glob("*.xlsx"):
        wb = openpyxl.load_workbook(arq)
        for ws in wb.worksheets:
            for linha in ws.iter_rows():
                for c in linha:
                    if isinstance(c.value, str) and prefixo in c.value:
                        c.value = c.value.replace(prefixo, "")
        wb.save(arq)


if __name__ == "__main__":
    nb, no = gerar_selecao()
    ne = gerar_extracao()
    print(f"Seleção: {nb} registros das bases + {no} de outras fontes | Extração: {ne} estudos")
    compilar("selecao")
    compilar("extracao")
