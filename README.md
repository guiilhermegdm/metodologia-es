# Agentes Multimodais para Educação Inclusiva, Neurodiversidade e Computação Afetiva

Mapeamento sistemático da literatura (tema 6) sobre agentes que processam múltiplas modalidades (texto, voz, expressões faciais, olhar, sinais fisiológicos e métricas de interação) para:

- detectar estados afetivos (frustração, tédio, sobrecarga cognitiva);
- adaptar o ritmo, o formato e o tom das explicações para estudantes neurodivergentes (TEA, TDAH, dislexia) ou com deficiências sensoriais.

## Questões de pesquisa

- **QP1:** Quais mecanismos de inferência afetiva e percepção multimodal são integrados aos agentes para monitorar o engajamento emocional do estudante em tempo real?
- **QP2:** Quais estratégias de personalização do conteúdo demonstraram ser mais eficazes para reduzir a ansiedade de aprendizagem em perfis neurodivergentes?

Como este é um mapeamento, e não uma revisão com meta-análise, a QP2 é respondida de forma descritiva: estratégias aplicadas × desfechos relatados × rigor da avaliação. A operacionalização está na [Seção 2.1 do protocolo](protocolo/PROTOCOLO.md#21-como-a-qp2-é-respondida-neste-mapeamento).

## Situação da entrega

O plano de ensino pede que o grupo **planeje, execute e documente** um estudo secundário sistemático. Situação de cada etapa:

| Etapa | Situação | Onde está |
|---|---|---|
| Planejamento (questões, string, fontes, critérios, esquema de classificação) | Concluído | [`protocolo/PROTOCOLO.md`](protocolo/PROTOCOLO.md) |
| Busca nas bases indexadas (IEEE Xplore e ACM DL) | Concluída em 05/11/2026 (383 registros) | `estudos-primarios-coletados/bases-indexadas/` |
| Seleção por busca acadêmica e *snowballing* | Concluída (46 candidatos, 25 incluídos) | `estudos-primarios-coletados/selecao-estudos.csv` |
| Triagem dos registros das bases | **Pendente** (378 registros) | `estudos-primarios-coletados/triagem-bases.csv` |
| Concordância entre revisores (kappa de Cohen) | **Pendente**; procedimento e script prontos | [Seção 5.1 do protocolo](protocolo/PROTOCOLO.md#51-procedimento-para-a-triagem-pendente-e-concordância-entre-revisores) e `synesis/scripts/concordancia.py` |
| Extração e classificação dos incluídos | Concluída para os 25 estudos | `dados/extracao-estudos-incluidos.csv` |
| Relatório automatizado | Concluído | `synesis/saida/relatorio.md` |
| Artigo (SBC, ERI-GO 2026) | Submetido; será anexado após a revisão cega | Seção [Artigo](#artigo) |

## Estrutura do repositório

```
.
├── README.md                          ← este arquivo
├── .gitattributes                     ← normalização de finais de linha (CSV em CRLF)
├── protocolo/
│   └── PROTOCOLO.md                   ← questões, strings, fontes, critérios e esquema de classificação
├── estudos-primarios-coletados/
│   ├── README.md                      ← como os dados foram coletados
│   ├── bases-indexadas/
│   │   ├── ieee-xplore.bib            ← 367 registros retornados pela string
│   │   └── acm-digital-library.bib    ← 16 registros retornados pela string
│   ├── outras-fontes/
│   │   ├── candidatos-avaliados.bib   ← candidatos da busca acadêmica e do snowballing
│   │   └── candidatos-sem-metadados.bib ← 10 excluídos sem metadados verificados (só rastreio)
│   ├── estudos-incluidos.bib          ← 25 estudos primários incluídos
│   ├── selecao-estudos.csv            ← decisão (incluído/excluído) e critério de cada candidato
│   └── triagem-bases.csv              ← planilha de triagem dos 383 registros das bases
├── dados/
│   └── extracao-estudos-incluidos.csv ← classificação dos 25 estudos (facetas do mapeamento)
└── synesis/                           ← automação do mapeamento com Synesis
    ├── README.md                      ← como rodar e como registrar a triagem
    ├── selecao/                       ← projeto Synesis da seleção (template com critérios CI/CE)
    ├── extracao/                      ← projeto Synesis da extração (template + ontologia)
    ├── scripts/                       ← gerar_projetos.py, relatorio.py e concordancia.py
    ├── requirements.txt               ← dependências dos scripts
    └── saida/                         ← CSV, Excel, JSON e relatorio.md compilados
```

## Automação com Synesis

O processo do mapeamento é automatizado com o compilador [Synesis](https://pypi.org/project/synesis/):

```bash
cd synesis
pip install -r requirements.txt    # synesis + openpyxl
python scripts/gerar_projetos.py   # deduplica, gera as anotações e compila seleção e extração
python scripts/relatorio.py        # funil da seleção e frequências por faceta (saida/relatorio.md)
```

O compilador confere três coisas:
- se cada decisão e cada classificação aponta para um registro existente nos `.bib`;
- se critérios e categorias usam apenas os valores definidos nos templates;
- se os códigos de modalidade, estado e adaptação pertencem à ontologia.

Os detalhes estão em [`synesis/README.md`](synesis/README.md).

## Resumo dos números

| Etapa | Quantidade |
|---|---|
| Registros retornados nas bases indexadas (IEEE Xplore + ACM DL, 05/11/2026) | 383 |
| Duplicatas removidas automaticamente (Synesis) | 5 |
| Registros das bases pendentes de triagem por título e resumo | 378 |
| Candidatos avaliados na elegibilidade (busca acadêmica + *snowballing*) | 46 |
| Estudos excluídos (CE1: 9 · CE2: 2 · CE3: 7 · CE4: 3) | 21 |
| **Estudos primários incluídos** | **25** |

## Principais resultados

- O TEA concentra 48% dos estudos incluídos. Nenhum estudo trata de estudantes cegos ou com baixa visão.
- As modalidades mais usadas são olhar, sinais fisiológicos/EEG e métricas de interação.
- Os agentes inferem sobretudo engajamento e atenção, com aprendizado de máquina clássico ou regras.
- A evidência direta de redução da ansiedade é escassa. Os resultados mais consistentes vêm de três estratégias:
  - adaptação da dificuldade guiada pelo engajamento;
  - *feedback* afetivo;
  - ajuste de ritmo e formato.

## Como reutilizar os dados

- **Arquivos `.bib`:** importe no Zotero, Mendeley, JabRef, Parsifal ou StArt para fazer a triagem.
- **Arquivos `.csv`:** abra no Excel, LibreOffice ou Google Sheets (codificação UTF-8).

## Artigo

Os resultados deste mapeamento foram submetidos como artigo completo (modelo SBC, 8 a 10 páginas) à XIV Escola Regional de Informática de Goiás ([ERI-GO 2026](http://erigo.sbc.org.br/p/128-chamadas-de-trabalhos)), com revisão duplo-cega. Por isso, o PDF e os fontes LaTeX só serão adicionados a este repositório depois da divulgação do resultado, para não identificar a autoria durante a revisão.

## Como contribuir

1. Atualize o repositório local antes de começar (`git pull`).
2. Registre decisões de triagem em `estudos-primarios-coletados/triagem-bases.csv` e classificações em `dados/extracao-estudos-incluidos.csv`.
3. Rode `python scripts/gerar_projetos.py` e `python scripts/relatorio.py` (na pasta `synesis/`) e confira se a compilação passa sem erros.
4. Na triagem, siga o procedimento de dupla revisão da [Seção 5.1 do protocolo](protocolo/PROTOCOLO.md#51-procedimento-para-a-triagem-pendente-e-concordância-entre-revisores) e registre o kappa obtido com `python scripts/concordancia.py kappa ...`.
5. Faça commits pequenos, com mensagens no imperativo que digam o que mudou (por exemplo, `dados: classifica estudos da triagem do IEEE`).
