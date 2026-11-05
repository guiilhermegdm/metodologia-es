# Automação do mapeamento sistemático com Synesis

Esta pasta usa o [Synesis](https://pypi.org/project/synesis/) para automatizar e validar as etapas do mapeamento sistemático. O Synesis é uma linguagem e um compilador para anotações de pesquisa. Ele recebe:

- a bibliografia (`.bib`);
- um template com os campos permitidos (`.synt`);
- uma ontologia com o vocabulário controlado (`.syno`);
- as anotações de cada estudo (`.syn`).

Ao compilar, ele confere se tudo está consistente e exporta tabelas em CSV, Excel e JSON. Se houver algum erro (uma chave inexistente no `.bib`, um valor fora da lista permitida, um código que não está na ontologia), **nenhuma saída é gerada**.

## Projetos

| Projeto | Fase do mapeamento | O que cada bloco representa |
|---|---|---|
| `selecao/selecao.synp` | Identificação, deduplicação, triagem e elegibilidade | Um `SOURCE` por registro coletado (base de origem e duplicata) e um `ITEM` com a decisão (etapa, decisão, critério e justificativa) |
| `extracao/extracao.synp` | Extração e classificação (QP1 e QP2) | Um `SOURCE` por estudo incluído (população, agente, técnica, fusão, tempo real, avaliação e N) e um `ITEM` com síntese, desfecho afetivo e códigos de modalidade, estado e adaptação |

### O que o compilador garante

- Toda decisão e toda extração apontam para uma chave existente nos `.bib` coletados.
- Decisão, critério (CI, CE1–CE4, DUP), população, tipo de agente, técnica, fusão e avaliação só aceitam os valores definidos nos templates.
- Modalidades (`mod_*`), estados (`est_*`) e adaptações (`adp_*`) só aceitam códigos definidos em `extracao/ontologia.syno`.
- Os templates descrevem os critérios de inclusão e exclusão e trazem orientações (`GUIDELINES`) para quem faz a triagem.

## Como rodar

```bash
cd synesis
pip install -r requirements.txt    # synesis + openpyxl
python scripts/gerar_projetos.py   # gera as anotações a partir dos dados e compila os dois projetos
python scripts/relatorio.py        # gera saida/relatorio.md com o funil e as frequências por faceta
```

O script `gerar_projetos.py` executa automaticamente estas etapas:

1. Lê os `.bib` de `../estudos-primarios-coletados`.
2. **Deduplica** os registros das bases por DOI e título. Na coleta atual, encontrou 5 duplicatas: 4 já estavam entre os candidatos de outras fontes e 1 se repete dentro do próprio IEEE.
3. Cria ou atualiza `../estudos-primarios-coletados/triagem-bases.csv`, mantendo as decisões já preenchidas.
4. Gera `selecao/registros.syn` e `extracao/estudos.syn`, a partir de `../dados/extracao-estudos-incluidos.csv`.
5. Compila os dois projetos no modo `--strict` e salva as saídas em `saida/`.

## Como fazer a triagem dos registros das bases

1. Abra `../estudos-primarios-coletados/triagem-bases.csv`.
2. Para cada registro pendente, preencha:
   - `decisao`: `incluido` ou `excluido`;
   - `criterio`: `CI`, `CE1`, `CE2`, `CE3` ou `CE4`;
   - `justificativa`: um texto curto.
3. Rode `python scripts/gerar_projetos.py` e depois `python scripts/relatorio.py`.

Valores digitados errado (por exemplo, `CE5` ou `incluído` com acento) fazem a compilação falhar e indicam o arquivo e a linha do erro. Os incluídos na triagem devem então ser classificados em `../dados/extracao-estudos-incluidos.csv` para entrar no projeto de extração.

## Saídas (`saida/`)

| Arquivo | Conteúdo |
|---|---|
| `selecao/sources.csv`, `selecao/items.csv`, `selecao/selecao.xlsx`, `selecao/selecao.json` | Registros e decisões de seleção, com rastreabilidade até o arquivo e a linha de origem |
| `extracao/sources.csv`, `extracao/items.csv`, `extracao/ontologies.csv`, `extracao/extracao.xlsx`, `extracao/extracao.json` | Classificação dos 25 estudos incluídos |
| `relatorio.md` | Funil da seleção, frequência de cada faceta, tabelas cruzadas por população e desfechos afetivos |

As frequências do relatório reproduzem os números do artigo. Por exemplo: TEA em 12 de 25 estudos, aprendizado de máquina clássico em 10, fusão por decisão em 7 e tempo real em 17.

## Estrutura

```
synesis/
├── selecao/
│   ├── selecao.synt        ← template da seleção (critérios CI/CE e etapas)
│   ├── selecao.synp        ← projeto (gerado)
│   ├── registros.syn       ← decisões por registro (gerado)
│   └── bib/                ← cópia dos .bib coletados (gerado)
├── extracao/
│   ├── extracao.synt       ← template do esquema de classificação
│   ├── ontologia.syno      ← vocabulário controlado (modalidades, estados, adaptações)
│   ├── extracao.synp       ← projeto (gerado)
│   ├── estudos.syn         ← classificação por estudo (gerado)
│   └── bib/                ← estudos-incluidos.bib (gerado)
├── scripts/
│   ├── gerar_projetos.py   ← automação: deduplicação, geração e compilação
│   └── relatorio.py        ← relatório do mapeamento a partir das saídas do Synesis
├── requirements.txt        ← dependências (synesis, openpyxl)
└── saida/                  ← artefatos compilados
```
