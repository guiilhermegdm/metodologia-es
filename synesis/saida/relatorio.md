# Relatório do mapeamento sistemático (gerado pelo Synesis)

Gerado automaticamente por `scripts/relatorio.py` a partir dos artefatos compilados pelo Synesis.

## 1. Seleção de estudos

| Fonte | Registros | Duplicatas | Pendentes de triagem | Incluídos | Excluídos (CE1/CE2/CE3/CE4) |
|---|---|---|---|---|---|
| IEEE Xplore | 367 | 5 | 362 | 0 | 0 (0/0/0/0) |
| ACM Digital Library | 16 | 0 | 16 | 0 | 0 (0/0/0/0) |
| Outras fontes (busca acadêmica + snowballing) | 46 | 0 | 0 | 25 | 21 (9/2/7/3) |

**Total:** 429 registros · 5 duplicatas · 378 pendentes · 25 incluídos · 21 excluídos.

## 2. Classificação dos 25 estudos incluídos


### População

| Categoria | Estudos | % |
|---|---|---|
| TEA | 12 | 48% |
| TDAH | 6 | 24% |
| DI | 2 | 8% |
| Misto | 2 | 8% |
| Dislexia | 2 | 8% |
| Surdez | 1 | 4% |

### Tipo de agente

| Categoria | Estudos | % |
|---|---|---|
| rv_avatar | 7 | 28% |
| robo_social | 5 | 20% |
| jogo_serio | 5 | 20% |
| sti | 3 | 12% |
| agente_virtual | 3 | 12% |
| chatbot_llm | 1 | 4% |
| sistema_adaptativo | 1 | 4% |

### Técnica de inferência (QP1.3)

| Categoria | Estudos | % |
|---|---|---|
| ml_classico | 10 | 40% |
| regras_limiares | 7 | 28% |
| nao_informado | 4 | 16% |
| deep_learning | 3 | 12% |
| dl_llm | 1 | 4% |

### Nível de fusão (QP1.3)

| Categoria | Estudos | % |
|---|---|---|
| unimodal | 9 | 36% |
| decisao | 7 | 28% |
| nao_informado | 5 | 20% |
| atributos | 3 | 12% |
| hibrida | 1 | 4% |

### Inferência em tempo real (QP1.4)

| Categoria | Estudos | % |
|---|---|---|
| sim | 17 | 68% |
| nao | 5 | 20% |
| nao_informado | 3 | 12% |

### Tipo de avaliação (QP2.3)

| Categoria | Estudos | % |
|---|---|---|
| Laboratório | 8 | 32% |
| Experimento controlado | 8 | 32% |
| Campo | 5 | 20% |
| Prova de conceito | 4 | 16% |

### Modalidades (QP1.1)

| Categoria | Estudos | % |
|---|---|---|
| Sinais fisiológicos (EDA, frequência cardíaca, EEG, temperatura) (`mod_fisiologico`) | 12 | 48% |
| Direção do olhar ou rastreamento ocular, incluindo pupilometria (`mod_olhar`) | 12 | 48% |
| Métricas de interação: desempenho, tempos de resposta, cliques, logs (`mod_interacao_logs`) | 12 | 48% |
| Expressões faciais captadas por câmera (`mod_face`) | 8 | 32% |
| Postura corporal, movimentos de cabeça e gestos (`mod_postura_gestos`) | 7 | 28% |
| Fala e prosódia (tom, ritmo, intensidade da voz) (`mod_voz`) | 6 | 24% |
| Texto digitado ou escrito pelo estudante (`mod_texto`) | 1 | 4% |

### Modalidades × população

| | TEA | TDAH | Dislexia | DI | Surdez | Baixa_visao | Misto | Total |
|---|---|---|---|---|---|---|---|---|
| mod_fisiologico | 8 | 4 | · | · | · | · | · | 12 |
| mod_olhar | 7 | 1 | 1 | 2 | · | · | 1 | 12 |
| mod_interacao_logs | 6 | 2 | 1 | 2 | · | · | 1 | 12 |
| mod_face | 4 | 1 | · | 1 | 1 | · | 1 | 8 |
| mod_postura_gestos | 4 | · | · | 1 | 1 | · | 1 | 7 |
| mod_voz | 3 | · | 1 | 1 | · | · | 1 | 6 |
| mod_texto | · | · | 1 | · | · | · | · | 1 |

### Estados inferidos (QP1.2)

| Categoria | Estudos | % |
|---|---|---|
| Engajamento com a tarefa ou com o agente (`est_engajamento`) | 12 | 48% |
| Atenção ou desatenção sustentada (`est_atencao`) | 9 | 36% |
| Frustração (`est_frustracao`) | 4 | 16% |
| Emoções básicas (alegria, tristeza, raiva etc.) (`est_emocoes_basicas`) | 3 | 12% |
| Tédio (`est_tedio`) | 2 | 8% |
| Carga cognitiva ou sobrecarga (`est_carga_cognitiva`) | 2 | 8% |
| Ansiedade ou estresse (`est_ansiedade`) | 2 | 8% |
| Dimensões de valência e ativação (arousal) (`est_valencia_ativacao`) | 1 | 4% |
| Prazer ou divertimento (`est_prazer`) | 1 | 4% |
| Confusão (`est_confusao`) | 1 | 4% |
| Inatividade ou ausência de resposta (`est_inatividade`) | 1 | 4% |
| Confiança percebida (`est_confianca`) | 1 | 4% |
| Interesse (`est_interesse`) | 1 | 4% |

### Estados inferidos × população

| | TEA | TDAH | Dislexia | DI | Surdez | Baixa_visao | Misto | Total |
|---|---|---|---|---|---|---|---|---|
| est_engajamento | 9 | · | · | 1 | 1 | · | 1 | 12 |
| est_atencao | 1 | 6 | 1 | 1 | · | · | · | 9 |
| est_frustracao | 1 | · | · | 1 | · | · | 2 | 4 |
| est_emocoes_basicas | 1 | · | 1 | · | 1 | · | · | 3 |
| est_tedio | 1 | · | · | 1 | · | · | · | 2 |
| est_carga_cognitiva | 1 | 1 | · | · | · | · | · | 2 |
| est_ansiedade | 1 | · | · | · | · | · | 1 | 2 |
| est_valencia_ativacao | 1 | · | · | · | · | · | · | 1 |
| est_prazer | 1 | · | · | · | · | · | · | 1 |
| est_confusao | · | · | · | · | · | · | 1 | 1 |
| est_inatividade | · | · | 1 | · | · | · | · | 1 |
| est_confianca | · | · | · | · | · | · | 1 | 1 |
| est_interesse | · | · | · | · | · | · | 1 | 1 |

### Estratégias de adaptação (QP2.1)

| Categoria | Estudos | % |
|---|---|---|
| Ajuste de tom ou feedback afetivo e motivacional (`adp_tom_feedback`) | 9 | 36% |
| Ajuste de dificuldade ou seleção de conteúdo (`adp_dificuldade`) | 8 | 32% |
| Ajuste de ritmo, velocidade ou pausas (`adp_ritmo`) | 7 | 28% |
| O agente apenas detecta o estado, sem adaptar a interação (`adp_apenas_deteccao`) | 6 | 24% |
| Mudança de formato ou modalidade de apresentação do conteúdo (`adp_formato`) | 5 | 20% |
| Estratégias explícitas de regulação emocional (`adp_regulacao_emocional`) | 1 | 4% |

### Estratégias de adaptação × população

| | TEA | TDAH | Dislexia | DI | Surdez | Baixa_visao | Misto | Total |
|---|---|---|---|---|---|---|---|---|
| adp_tom_feedback | 4 | 2 | 1 | 1 | · | · | 1 | 9 |
| adp_dificuldade | 4 | 2 | · | 1 | · | · | 1 | 8 |
| adp_ritmo | 1 | 4 | 2 | · | · | · | · | 7 |
| adp_apenas_deteccao | 5 | · | · | · | 1 | · | · | 6 |
| adp_formato | 2 | 1 | 1 | 1 | · | · | · | 5 |
| adp_regulacao_emocional | · | · | · | · | · | · | 1 | 1 |

## 3. Desfechos afetivos relatados (QP2.2)

| Estudo | População | Adaptação | Desfecho relatado |
|---|---|---|---|
| S01 `rudovic2018personalized` | TEA | adp_apenas_deteccao | Modelos personalizados estimaram afeto e engajamento melhor que modelos não personalizados; não houve adaptação do robô em tempo real. |
| S02 `jain2020modeling` | TEA | adp_apenas_deteccao | Detecção post hoc de engajamento com AUROC ~90%; padrões temporais das predições poderiam disparar ações de reengajamento, mas não foram implantados online. |
| S03 `javed2020toward` | TEA | adp_apenas_deteccao | Acurácia média ~0,78 (F1 0,76) na estimativa de engajamento; RF obteve 0,81; métrica não foi usada para adaptar o robô. |
| S04 `esteban2017build` | TEA | adp_ritmo, adp_tom_feedback | não avaliado (artigo de arquitetura; o robô tenta reengajar a criança quando o engajamento estimado é baixo antes de avançar no roteiro). |
| S05 `bekele2013step` | TEA | adp_formato, adp_tom_feedback | Crianças (TEA e típicas) olharam mais para o robô do que para o terapeuta humano; não houve mensuração de ansiedade/frustração. |
| S06 `lahiri2011design` | TEA | adp_tom_feedback | Engajamento avaliado pelo cuidador tendeu a aumentar em tentativas posteriores (5/6); maior engajamento associado a mais olhar para a face; apenas estatística descritiva. |
| S07 `lahiri2013design` | TEA | adp_dificuldade, adp_tom_feedback | Engajamento quantificado em tempo real; resultados preliminares indicam potencial para melhorar desempenho em tarefas sociais e padrões de olhar. |
| S08 `lahiri2015physiologically` | TEA | adp_dificuldade, adp_formato | Sistema sensível à fisiologia levou a melhor desempenho conversacional e padrões de olhar do que o sistema baseado apenas em desempenho. |
| S09 `bian2015physiology` | TEA | adp_apenas_deteccao | Modelos de reconhecimento afetivo produziram predições confiáveis (sem números no resumo); propostos como base para treino adaptativo de direção. |
| S10 `bian2019design` | TEA | adp_dificuldade | Grupo sensível ao engajamento teve índice de engajamento maior (0,78 vs 0,51; p=0,03) e gostou mais dos ajustes; sem diferenças significativas em frustração, tédio ou desempenho. |
| S11 `zhang2015multimodal` | TEA | adp_apenas_deteccao | não avaliado (foco na acurácia de detecção de carga cognitiva, melhor resultado 84,66% com fusão híbrida). |
| S12 `kuriakose2017design` | TEA | adp_dificuldade | Estudo preliminar de usabilidade sugeriu melhora no desempenho nas tarefas; resultados específicos de ansiedade não detalhados no resumo. |
| S13 `standen2020evaluation` | DI | adp_dificuldade, adp_formato | Engajamento significativamente maior e tédio significativamente menor nas sessões com adaptação afetiva; sem diferença significativa no desempenho. |
| S14 `boulton2018multi` | Misto | adp_dificuldade | Relata achados iniciais e desafios de captura multimodal em sala de aula; desfechos afetivos não quantificados no resumo. |
| S15 `lim2012brain` | TDAH | adp_ritmo | Pais relataram redução significativa de sintomas de desatenção e hiperatividade-impulsividade; afeto/ansiedade não avaliados. |
| S16 `lim2019randomized` | TDAH | adp_ritmo | Melhora pequena porém significativa na desatenção (ADHD-RS) e maior melhora em problemas internalizantes (CBCL) no grupo intervenção; ansiedade não avaliada isoladamente. |
| S17 `huang2023effective` | TDAH | adp_ritmo, adp_dificuldade | Piloto relatou melhora da atenção após o treino; afeto não avaliado. |
| S18 `johnstone2017game` | TDAH | adp_tom_feedback | Prazer e engajamento declinaram ao longo das sessões; sintomas de TDAH reduziram segundo pais (e professores no grupo TDAH). |
| S19 `schiavo2021attention` | Dislexia | adp_ritmo, adp_formato | não avaliado (compreensão leitora de crianças com dislexia melhorou 24%). |
| S20 `richter2024vaco` | TDAH | adp_tom_feedback, adp_dificuldade | SUS médio 78,9; cerca de metade das crianças achou Flobi motivador; ansiedade/frustração não avaliadas. |
| S21 `leichert2025virtual` | DI | adp_tom_feedback | Tempo atento permaneceu alto para a maioria, mas o estudo de uma semana foi curto para mostrar melhora de atenção; limite de duas tentativas introduzido para reduzir frustração. |
| S22 `piferi2025integrating` | Dislexia | adp_tom_feedback, adp_ritmo | não avaliado. |
| S23 `woolf2010effect` | Misto | adp_tom_feedback, adp_regulacao_emocional | Após interagir com os agentes afetivos, estudantes de baixo desempenho (incluindo com dificuldades de aprendizagem) reduziram frustração e ansiedade. |
| S24 `rupasinghe2026interactive` | Surdez | adp_apenas_deteccao | Reporta acurácia de validação de 96,9% para o modelo facial e maior robustez na detecção de engajamento; desfechos afetivos em usuários não avaliados. |
| S25 `navneet2026orchestrating` | TDAH | adp_formato, adp_ritmo | Condição adaptativa reduziu a carga cognitiva (NASA-TLX 47,2 vs 62,8; d=1,21; p=0,008) e aumentou a compreensão (78,4% vs 61,2%; p=0,009). |
