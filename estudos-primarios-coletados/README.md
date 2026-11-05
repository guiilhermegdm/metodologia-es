# Estudos primários coletados

Esta pasta reúne todos os dados bibliográficos coletados no mapeamento sistemático sobre **agentes multimodais para educação inclusiva, neurodiversidade e computação afetiva**: os registros retornados pelas strings de busca nas bases indexadas e os estudos candidatos vindos de outras fontes, com a decisão de seleção de cada um.

## Conteúdo

| Arquivo | O que contém | Registros |
|---|---|---|
| `bases-indexadas/ieee-xplore.bib` | Todos os registros retornados pela string no IEEE Xplore | 367 |
| `bases-indexadas/acm-digital-library.bib` | Todos os registros retornados pela string na ACM Digital Library | 16 |
| `outras-fontes/candidatos-avaliados.bib` | Candidatos da busca acadêmica e do *snowballing* com metadados verificados | 36 |
| `outras-fontes/candidatos-sem-metadados.bib` | Marcadores dos 10 candidatos excluídos cujos metadados não foram verificados (servem só para rastrear a decisão; não citar) | 10 |
| `estudos-incluidos.bib` | Estudos primários incluídos no mapeamento (S01–S25 no artigo) | 25 |
| `selecao-estudos.csv` | Decisão de seleção dos 46 candidatos avaliados (incluídos e excluídos, com critério e justificativa) | 46 |
| `triagem-bases.csv` | Planilha de triagem dos 383 registros das bases, com as duplicatas já marcadas; gerada e atualizada por `synesis/scripts/gerar_projetos.py` | 383 |

**Chaves BibTeX:** as entradas das bases receberam o prefixo da base (`ieee7344544`, `acm_3850153`). O motivo é que a chave original da ACM é o DOI, e a barra do DOI não é aceita pelo Synesis.

Os arquivos `.bib` podem ser importados diretamente no Zotero, Mendeley, JabRef, Parsifal ou StArt.

## Como os dados foram obtidos

### Bases indexadas (busca em 05/11/2026)

String de busca, com as aspas e os operadores aplicados em cada base:

```
("agent" OR "tutor*" OR "robot*" OR "chatbot" OR "serious game")
AND ("affect*" OR "emotion*" OR "engagement" OR "frustration" OR "anxiety" OR "cognitive load")
AND ("multimodal" OR "facial expression" OR "gaze" OR "eye tracking" OR "physiological" OR "EEG" OR "speech")
AND ("autism" OR "ADHD" OR "dyslexia" OR "intellectual disability" OR "learning disability"
     OR "neurodivergent" OR "deaf" OR "hearing impairment" OR "visual impairment" OR "blind")
```

| Base | Campo pesquisado | Filtros | Registros |
|---|---|---|---|
| IEEE Xplore | *All Metadata* (título, resumo e termos de indexação) | Ano de publicação 2010–2026 | 367 |
| ACM Digital Library | *Abstract* | Data de publicação 2010–2026; ACM Full-Text Collection | 16 |
| **Total** | | | **383** (sem duplicatas por DOI entre as bases) |

- **IEEE Xplore:** BibTeX gerado pela função de exportação de citações da própria base (formato *citation only*). Foram removidos apenas os campos `url`, `keywords` e `volume`/`number` vazios.
- **ACM DL:** citações exportadas pela própria base e convertidas para BibTeX, sem alterar os dados.
- **Registros que não são artigos:** seis registros do IEEE não têm autor. São normas, sumários e páginas iniciais de anais. Foram mantidos porque fazem parte do retorno bruto da string e devem ser removidos na triagem.

### Outras fontes (busca acadêmica e *snowballing*)

A seleção relatada no artigo partiu de buscas acadêmicas com restrição aos domínios das bibliotecas digitais (IEEE Xplore, ACM DL, SpringerLink, ScienceDirect, PubMed/PMC, Frontiers, PLoS, MDPI e arXiv), complementadas por *snowballing* retroativo e prospectivo. Desse processo saíram 46 candidatos únicos:

- **25 incluídos**, todos em `estudos-incluidos.bib`.
- **21 excluídos:** 11 com BibTeX verificado e 10 registrados apenas pela descrição na planilha de seleção, porque seus metadados não foram verificados.

Três desses candidatos também aparecem no retorno do IEEE Xplore (coluna `tambem_retornado_nas_bases` do CSV).

## Critérios de seleção

- **CI1:** estudo primário que propõe, implementa ou avalia um agente (STI, agente virtual/avatar, robô social, *chatbot*/LLM, jogo sério ou sistema adaptativo) para estudantes neurodivergentes ou com deficiência sensorial.
- **CI2:** o agente infere automaticamente ao menos um estado afetivo, atencional ou cognitivo a partir de sinais do estudante.
- **CI3:** contexto de aprendizagem, treino de habilidades ou intervenção educacional.
- **CE1:** ausência de inferência automática de estado.
- **CE2:** não há agente ou não há dados do estudante.
- **CE3:** população, contexto ou desenho fora do escopo.
- **CE4:** texto ou metadados não verificáveis; estudos secundários; duplicatas.

## Situação da triagem

Os 383 registros das bases indexadas foram coletados depois da seleção relatada no artigo.

- **Deduplicação automática:** feita pelo Synesis (pasta `synesis/`). Encontrou 5 duplicatas:
  - 4 registros do IEEE que já estavam entre os candidatos de outras fontes: MASI-VR, Li et al. 2025, Rupasinghe et al. 2026 e Leichert et al., cujo *preprint* incluído no mapeamento foi publicado no IEEE;
  - 1 registro repetido dentro do próprio IEEE.
- **Triagem por título e resumo:** os 378 registros restantes **ainda não passaram por ela**. As decisões devem ser registradas em `triagem-bases.csv`, conforme explicado em `synesis/README.md`.
