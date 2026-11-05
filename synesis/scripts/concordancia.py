"""Concordância entre revisores na seleção de estudos (kappa de Cohen).

Uso (a partir da pasta synesis/):

    # 1. Sorteia uma amostra para o segundo revisor avaliar às cegas
    python scripts/concordancia.py amostra --origem ../estudos-primarios-coletados/selecao-estudos.csv \
        --tamanho 15 --saida ../estudos-primarios-coletados/revisor-b.csv

    # 2. O segundo revisor preenche a coluna "decisao" (incluido/excluido) do arquivo gerado

    # 3. Compara as decisões do segundo revisor com as decisões registradas
    python scripts/concordancia.py kappa --revisor-a ../estudos-primarios-coletados/selecao-estudos.csv \
        --revisor-b ../estudos-primarios-coletados/revisor-b.csv

A comparação usa apenas os registros com decisão "incluido" ou "excluido" nos dois
arquivos (com ou sem acento). Registros "pendente" e "duplicata" são ignorados.
Não depende de bibliotecas externas.
"""

import argparse
import csv
import random
import sys
import unicodedata
from pathlib import Path

DECISOES = {"incluido", "excluido"}


def normaliza(texto):
    """Remove acentos, espaços e caixa: 'Incluído ' -> 'incluido'."""
    sem_acento = unicodedata.normalize("NFKD", texto or "")
    sem_acento = "".join(c for c in sem_acento if not unicodedata.combining(c))
    return sem_acento.strip().lower()


def le_csv(caminho):
    with open(caminho, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def decisoes(caminho):
    """Mapeia chave_bibtex -> decisão normalizada, só para incluído/excluído."""
    resultado = {}
    for linha in le_csv(caminho):
        decisao = normaliza(linha.get("decisao"))
        chave = (linha.get("chave_bibtex") or "").strip()
        if chave and decisao in DECISOES:
            resultado[chave] = decisao
    return resultado


def kappa_cohen(pares):
    """Kappa de Cohen para pares (decisao_a, decisao_b)."""
    n = len(pares)
    if n == 0:
        raise ValueError("nenhum registro em comum com decisão nos dois arquivos")
    concordancia = sum(a == b for a, b in pares) / n
    esperada = 0.0
    for categoria in DECISOES:
        p_a = sum(a == categoria for a, _ in pares) / n
        p_b = sum(b == categoria for _, b in pares) / n
        esperada += p_a * p_b
    if esperada == 1.0:
        return concordancia, esperada, 1.0
    return concordancia, esperada, (concordancia - esperada) / (1 - esperada)


def interpreta(kappa):
    """Faixas de Landis e Koch (1977)."""
    faixas = [(0.0, "pobre"), (0.20, "leve"), (0.40, "razoável"),
              (0.60, "moderada"), (0.80, "substancial"), (1.01, "quase perfeita")]
    for limite, rotulo in faixas:
        if kappa <= limite:
            return rotulo
    return "quase perfeita"


def cmd_amostra(args):
    linhas = [l for l in le_csv(args.origem) if normaliza(l.get("decisao")) in DECISOES]
    if args.tamanho > len(linhas):
        sys.exit(f"Amostra maior que o número de registros com decisão ({len(linhas)}).")
    sorteio = random.Random(args.semente).sample(linhas, args.tamanho)
    with open(args.saida, "w", encoding="utf-8-sig", newline="") as f:
        escritor = csv.writer(f)
        escritor.writerow(["chave_bibtex", "titulo", "decisao", "criterio", "justificativa"])
        for linha in sorted(sorteio, key=lambda l: l["chave_bibtex"]):
            escritor.writerow([linha["chave_bibtex"], linha.get("titulo", ""), "", "", ""])
    print(f"{args.tamanho} registros sorteados (semente {args.semente}) em {args.saida}.")
    print("O segundo revisor deve preencher 'decisao' sem consultar as decisões originais.")


def cmd_kappa(args):
    a, b = decisoes(args.revisor_a), decisoes(args.revisor_b)
    comuns = sorted(set(a) & set(b))
    pares = [(a[k], b[k]) for k in comuns]
    concordancia, esperada, kappa = kappa_cohen(pares)
    print(f"Registros comparados: {len(pares)}")
    print(f"Concordância observada: {concordancia:.1%}")
    print(f"Concordância esperada ao acaso: {esperada:.1%}")
    print(f"Kappa de Cohen: {kappa:.2f} ({interpreta(kappa)}, Landis e Koch, 1977)")
    divergentes = [k for k in comuns if a[k] != b[k]]
    if divergentes:
        print("\nDivergências a resolver por consenso:")
        for chave in divergentes:
            print(f"  - {chave}: revisor A = {a[chave]}, revisor B = {b[chave]}")


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="comando", required=True)

    p_amostra = sub.add_parser("amostra", help="sorteia registros para o segundo revisor")
    p_amostra.add_argument("--origem", type=Path, required=True)
    p_amostra.add_argument("--tamanho", type=int, required=True)
    p_amostra.add_argument("--saida", type=Path, required=True)
    p_amostra.add_argument("--semente", type=int, default=2026)
    p_amostra.set_defaults(func=cmd_amostra)

    p_kappa = sub.add_parser("kappa", help="calcula o kappa de Cohen entre dois revisores")
    p_kappa.add_argument("--revisor-a", type=Path, required=True)
    p_kappa.add_argument("--revisor-b", type=Path, required=True)
    p_kappa.set_defaults(func=cmd_kappa)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
