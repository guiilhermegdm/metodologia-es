# Protocolo do mapeamento sistemático

**Tema 6:** Agentes Multimodais para Educação Inclusiva, Neurodiversidade e Computação Afetiva

**Método:** mapeamento sistemático segundo Petersen et al. (2008, 2015), com *snowballing* segundo Wohlin (2014).

## 1. Objetivo e escopo

Mapear o uso de agentes capazes de processar múltiplas modalidades (texto, voz, expressões faciais, olhar, sinais fisiológicos e métricas de interação) para:

- detectar estados afetivos, como frustração, tédio, ansiedade e sobrecarga cognitiva;
- adaptar o ritmo, o formato e o tom das explicações para estudantes neurodivergentes (TEA, TDAH, dislexia, deficiência intelectual) ou com deficiências sensoriais.

## 2. Questões de pesquisa

**QP1.** Quais mecanismos de inferência afetiva e percepção multimodal são integrados aos agentes para monitorar o engajamento emocional do estudante em tempo real?

- QP1.1 Quais modalidades são capturadas?
- QP1.2 Quais estados afetivos ou cognitivos são inferidos?
- QP1.3 Quais técnicas de inferência e níveis de fusão são empregados?
- QP1.4 A inferência ocorre em tempo real?

**QP2.** Quais estratégias de personalização do conteúdo demonstraram ser mais eficazes para reduzir a ansiedade de aprendizagem em perfis neurodivergentes?

- QP2.1 Quais estratégias de adaptação são aplicadas (ritmo, formato, tom, dificuldade, regulação emocional)?
- QP2.2 Quais desfechos afetivos são relatados (ansiedade, frustração, tédio, engajamento, carga cognitiva)?
- QP2.3 Qual o rigor da avaliação empírica?

**Questões demográficas:** ano de publicação, população atendida e tipo de agente.

## 3. Estratégia de busca

### 3.1 String genérica

A string combina cinco blocos: agente, estado afetivo, modalidade, população e contexto de aprendizagem ou adaptação.

```
(agent* OR tutor* OR robot* OR chatbot OR "virtual human" OR "serious game" OR "intelligent tutoring")
AND (affect* OR emotion* OR engagement OR frustration OR boredom OR anxiety OR "cognitive load" OR attention)
AND (multimodal OR "facial expression" OR gaze OR "eye tracking" OR physiolog* OR EEG OR speech OR prosody OR "interaction log*")
AND (autism OR ASD OR ADHD OR dyslexia OR "intellectual disabilit*" OR "learning disabilit*" OR neurodivergen*
     OR deaf OR "hard of hearing" OR blind OR "visual impairment")
AND (adapt* OR personali* OR learning OR education* OR training)
```

### 3.2 String aplicada nas bases indexadas

A versão aplicada foi reduzida por causa dos limites de termos e curingas das bases:

```
("agent" OR "tutor*" OR "robot*" OR "chatbot" OR "serious game")
AND ("affect*" OR "emotion*" OR "engagement" OR "frustration" OR "anxiety" OR "cognitive load")
AND ("multimodal" OR "facial expression" OR "gaze" OR "eye tracking" OR "physiological" OR "EEG" OR "speech")
AND ("autism" OR "ADHD" OR "dyslexia" OR "intellectual disability" OR "learning disability"
     OR "neurodivergent" OR "deaf" OR "hearing impairment" OR "visual impairment" OR "blind")
```

### 3.3 Fontes

| Fonte | Campo | Período | Data da busca | Registros |
|---|---|---|---|---|
| IEEE Xplore | All Metadata | 2010–2026 | 05/11/2026 | 367 |
| ACM Digital Library | Abstract | 2010–2026 | 05/11/2026 | 16 |
| Busca acadêmica restrita aos domínios de IEEE Xplore, ACM DL, SpringerLink, ScienceDirect, PubMed/PMC, Frontiers, PLoS, MDPI e arXiv | Texto livre (4 substrings por subárea) | 2010–2026 | out/2026 | 46 candidatos após triagem |
| *Snowballing* retroativo e prospectivo | — | — | out/2026 | incluído na linha acima |

As quatro substrings da busca acadêmica cobrem estas subáreas:

1. TEA;
2. TDAH, dislexia e deficiência intelectual;
3. deficiências sensoriais;
4. agentes baseados em LLM.

## 4. Critérios de seleção

### Inclusão

- **CI1:** estudo primário que propõe, implementa ou avalia um agente (sistema tutor inteligente – STI, agente virtual/avatar, robô social, *chatbot*/LLM, jogo sério ou sistema adaptativo) para estudantes neurodivergentes ou com deficiência sensorial.
- **CI2:** o agente infere automaticamente ao menos um estado afetivo, atencional ou cognitivo a partir de sinais do estudante.
- **CI3:** contexto de aprendizagem, treino de habilidades ou intervenção educacional/terapêutico-educacional.

### Exclusão

- **CE1:** ausência de inferência automática de estado (p. ex., adaptação só por desempenho ou detecção feita por humanos).
- **CE2:** não há agente ou não há dados do estudante (p. ex., painéis sem adaptação, estudos só de percepção docente).
- **CE3:** população, contexto (p. ex., clínico-diagnóstico) ou desenho fora do escopo.
- **CE4:** texto completo ou metadados não verificáveis; estudos secundários; duplicatas.

## 5. Processo de seleção

1. Execução das strings e exportação dos registros em BibTeX (`estudos-primarios-coletados/`).
2. Remoção de duplicatas, comparando DOI e título.
3. Triagem por título e resumo, aplicando CI e CE.
4. Avaliação de elegibilidade pelo resumo e, quando necessário, pelo texto completo.
5. *Snowballing* retroativo e prospectivo a partir dos incluídos e das revisões relacionadas.

**Resultado relatado no artigo:** 46 candidatos únicos (após 4 duplicatas) → 21 excluídos (CE1: 9; CE2: 2; CE3: 7; CE4: 3) → **25 estudos incluídos**.

**Pendente:** triagem dos 378 registros das bases indexadas que restaram após a deduplicação automática (5 duplicatas), coletados em 05/11/2026. Esta etapa é registrada em `estudos-primarios-coletados/triagem-bases.csv` e automatizada com Synesis (ver `synesis/README.md`).

## 6. Esquema de classificação (extração de dados)

O esquema foi construído por *keywording* dos resumos.

| Faceta | Categorias |
|---|---|
| População | TEA, TDAH, dislexia, deficiência intelectual (DI), surdez, baixa visão, misto |
| Tipo de agente | STI, agente virtual/avatar, RV/avatar, robô social, *chatbot*/LLM, jogo sério, sistema adaptativo |
| Modalidades | texto, voz/prosódia, expressão facial, olhar, fisiológico/EEG, postura/gestos, interação/*logs* |
| Estados inferidos | engajamento, atenção, frustração, tédio, ansiedade, carga cognitiva, emoções básicas etc. |
| Técnica de inferência | regras/limiares, aprendizado de máquina clássico, *deep learning*, LLM |
| Nível de fusão | unimodal, atributos, decisão, híbrida |
| Tempo real | sim, não, não informado |
| Estratégia de adaptação | ritmo/pausas, formato/modalidade, tom/*feedback* afetivo, dificuldade/conteúdo, regulação emocional, apenas detecção |
| Tipo de avaliação | prova de conceito, estudo de laboratório, experimento controlado, estudo de campo |

Os dados extraídos estão em `dados/extracao-estudos-incluidos.csv`.

## 7. Ameaças à validade

- **Construto:** os termos "engajamento" e "agente" são usados de forma heterogênea na literatura. Por isso, o protocolo adota uma definição operacional de agente (CI1).
- **Completude:** a seleção relatada no artigo partiu de busca acadêmica e *snowballing*. A busca nas interfaces das bases (IEEE Xplore e ACM DL) foi executada depois e ainda precisa ser triada. Outras bases, como Scopus e Web of Science, não foram consultadas.
- **Seleção e extração:** campos ausentes nos estudos foram codificados como "não informado". Três estudos incluídos são *preprints*.
- **Conclusão:** as sínteses da QP2 são descritivas, e não meta-analíticas.
