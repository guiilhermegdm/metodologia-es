#!/usr/bin/env python3
"""Gera o relatório do mapeamento (saida/relatorio.md) a partir das saídas
compiladas pelo Synesis (saida/selecao/*.csv e saida/extracao/*.csv).

Uso (a partir da pasta synesis/, depois de rodar gerar_projetos.py):
    python scripts/relatorio.py
"""
import csv
from collections import Counter, defaultdict
from pathlib import Path

SYN = Path(__file__).resolve().parents[1]
SAIDA = SYN / "saida"


def ler(caminho):
    with open(caminho, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def chave(bibref):
    return bibref.lstrip("'").lstrip("@")


def tabela(titulo, contagem, total=None, cab=("Categoria", "Estudos")):
    linhas = [f"\n### {titulo}\n", f"| {cab[0]} | {cab[1]} |" + (" % |" if total else ""),
              "|---|---|" + ("---|" if total else "")]
    for k, v in contagem:
        linhas.append(f"| {k} | {v} |" + (f" {100 * v / total:.0f}% |" if total else ""))
    return linhas


def cruzada(titulo, linhas_cat, colunas, pares):
    out = [f"\n### {titulo}\n", "| | " + " | ".join(colunas) + " | Total |", "|---" * (len(colunas) + 2) + "|"]
    for l in linhas_cat:
        vals = [pares[(l, c)] for c in colunas]
        out.append(f"| {l} | " + " | ".join(str(v) if v else "·" for v in vals) + f" | {sum(vals)} |")
    return out


md = ["# Relatório do mapeamento sistemático (gerado pelo Synesis)", "",
      "Gerado automaticamente por `scripts/relatorio.py` a partir dos artefatos compilados pelo Synesis.", ""]

# ------------------------------------------------------------------ seleção
src = {chave(r["bibref"]): r for r in ler(SAIDA / "selecao" / "sources.csv")}
its = ler(SAIDA / "selecao" / "items.csv")
md.append("## 1. Seleção de estudos\n")
por_base = Counter(src[chave(i["bibref"])]["base"] for i in its)
dec = defaultdict(Counter)
for i in its:
    b = src[chave(i["bibref"])]["base"]
    dec[b][(i["decisao"], i["criterio"])] += 1
nomes = {"ieee_xplore": "IEEE Xplore", "acm_dl": "ACM Digital Library", "outras_fontes": "Outras fontes (busca acadêmica + snowballing)"}
md += ["| Fonte | Registros | Duplicatas | Pendentes de triagem | Incluídos | Excluídos (CE1/CE2/CE3/CE4) |",
       "|---|---|---|---|---|---|"]
for b in ["ieee_xplore", "acm_dl", "outras_fontes"]:
    d = dec[b]
    dup = sum(v for (x, _), v in d.items() if x == "duplicata")
    pen = sum(v for (x, _), v in d.items() if x == "pendente")
    inc = sum(v for (x, _), v in d.items() if x == "incluido")
    exc = [d[("excluido", c)] for c in ["CE1", "CE2", "CE3", "CE4"]]
    md.append(f"| {nomes[b]} | {por_base[b]} | {dup} | {pen} | {inc} | {sum(exc)} ({'/'.join(map(str, exc))}) |")
tot = Counter(i["decisao"] for i in its)
md += ["", f"**Total:** {len(its)} registros · {tot['duplicata']} duplicatas · {tot['pendente']} pendentes · "
       f"{tot['incluido']} incluídos · {tot['excluido']} excluídos.", ""]

# ------------------------------------------------------------------ extração
es = {chave(r["bibref"]): r for r in ler(SAIDA / "extracao" / "sources.csv")}
ei = {chave(r["bibref"]): r for r in ler(SAIDA / "extracao" / "items.csv")}
onto = {r["modalidade"] or r["estado"] or r["adaptacao"]: r for r in ler(SAIDA / "extracao" / "ontologies.csv")}
desc = {k: v["descricao"] for k, v in onto.items()}
N = len(es)
md.append(f"## 2. Classificação dos {N} estudos incluídos\n")
AVAL = {"1": "Prova de conceito", "2": "Laboratório", "3": "Experimento controlado", "4": "Campo"}
for campo, titulo in [("populacao", "População"), ("tipo_agente", "Tipo de agente"),
                      ("tecnica", "Técnica de inferência (QP1.3)"), ("fusao", "Nível de fusão (QP1.3)"),
                      ("tempo_real", "Inferência em tempo real (QP1.4)"), ("avaliacao", "Tipo de avaliação (QP2.3)")]:
    c = Counter(AVAL.get(r[campo], r[campo]) if campo == "avaliacao" else r[campo] for r in es.values())
    md += tabela(titulo, c.most_common(), N)

POPS = ["TEA", "TDAH", "Dislexia", "DI", "Surdez", "Baixa_visao", "Misto"]
for campo, titulo in [("modalidade", "Modalidades (QP1.1)"), ("estado", "Estados inferidos (QP1.2)"),
                      ("adaptacao", "Estratégias de adaptação (QP2.1)")]:
    c = Counter(cod for r in ei.values() for cod in r[campo].split(";") if cod)
    md += tabela(titulo, [(f"{desc.get(k, k)} (`{k}`)", v) for k, v in c.most_common()], N)
    pares = Counter((cod, es[k]["populacao"]) for k, r in ei.items() for cod in r[campo].split(";") if cod)
    md += cruzada(f"{titulo.split(' (')[0]} × população", [k for k, _ in c.most_common()], POPS, pares)

md += ["", "## 3. Desfechos afetivos relatados (QP2.2)", "",
       "| Estudo | População | Adaptação | Desfecho relatado |", "|---|---|---|---|"]
for k, r in sorted(es.items(), key=lambda x: x[1]["id_estudo"]):
    md.append(f"| {r['id_estudo']} `{k}` | {r['populacao']} | {ei[k]['adaptacao'].replace(';', ', ')} | {ei[k]['desfecho_afetivo']} |")

(SAIDA / "relatorio.md").write_text("\n".join(md) + "\n", encoding="utf-8")
print(f"Relatório gerado em {SAIDA / 'relatorio.md'}")
