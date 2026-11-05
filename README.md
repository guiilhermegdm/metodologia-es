# Agentes Multimodais para Educação Inclusiva, Neurodiversidade e Computação Afetiva

Mapeamento sistemático da literatura (tema 6) sobre agentes que processam múltiplas modalidades (texto, voz, expressões faciais, olhar, sinais fisiológicos e métricas de interação) para:

- detectar estados afetivos (frustração, tédio, sobrecarga cognitiva);
- adaptar o ritmo, o formato e o tom das explicações para estudantes neurodivergentes (TEA, TDAH, dislexia) ou com deficiências sensoriais.

## Questões de pesquisa

- **QP1:** Quais mecanismos de inferência afetiva e percepção multimodal são integrados aos agentes para monitorar o engajamento emocional do estudante em tempo real?
- **QP2:** Quais estratégias de personalização do conteúdo demonstraram ser mais eficazes para reduzir a ansiedade de aprendizagem em perfis neurodivergentes?

## Estrutura do repositório

```
.
├── README.md                          ← este arquivo
├── protocolo/
│   └── PROTOCOLO.md                   ← questões, strings, fontes, critérios e esquema de classificação
├── estudos-primarios-coletados/
│   ├── README.md                      ← como os dados foram coletados
│   ├── bases-indexadas/
│   │   ├── ieee-xplore.bib            ← 367 registros retornados pela string
│   │   └── acm-digital-library.bib    ← 16 registros retornados pela string
│   ├── outras-fontes/
│   │   └── candidatos-avaliados.bib   ← candidatos da busca acadêmica e do snowballing
│   │   └── candidatos-sem-metadados.bib
│   ├── estudos-incluidos.bib          ← 25 estudos primários incluídos
│   ├── selecao-estudos.csv            ← decisão (incluído/excluído) e critério de cada candidato
│   └── triagem-bases.csv              ← planilha de triagem dos 383 registros das bases
├── dados/
│   └── extracao-estudos-incluidos.csv ← classificação dos 25 estudos (facetas do mapeamento)
└── synesis/                           ← automação do mapeamento com Synesis
    ├── README.md                      ← como rodar e como registrar a triagem
    ├── selecao/                       ← projeto Synesis da seleção (template com critérios CI/CE)
    ├── extracao/                      ← projeto Synesis da extração (template + ontologia)
    ├── scripts/                       ← gerar_projetos.py e relatorio.py
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
