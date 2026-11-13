"""
EXPERIMENTO: efeito de acoplamento (Offutt, 1992) no exercicio 4.

Para cada PAR de mutantes de primeira ordem (que o mutmut gerou) em linhas
DIFERENTES, aplica as duas mudancas juntas e roda uma suite contra o
mutante de segunda ordem resultante.

Pergunta: dos mutantes de 2a ordem formados por dois mutantes de 1a ordem
que a suite JA MATA, quantos a suite tambem mata?

Rodar (da raiz do lab):  python ex4/extras/segunda_ordem_experimento.py
"""
import itertools
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
FONTE = (RAIZ / "ex4" / "src" / "multa.py").read_text().splitlines()

# (numero_no_mutmut, linha_original, linha_mutada) -- extraido de `mutmut show`
MUTANTES = [
    (1, 'if dias < 0 or dias > 60:', 'if dias < 0 and dias > 60:'),
    (2, 'if dias < 0 or dias > 60:', 'if dias <= 0 or dias > 60:'),
    (3, 'if dias < 0 or dias > 60:', 'if dias < 1 or dias > 60:'),
    (4, 'if dias < 0 or dias > 60:', 'if dias < 0 or dias >= 60:'),
    (5, 'if dias < 0 or dias > 60:', 'if dias < 0 or dias > 61:'),
    (6, 'raise ValueError("atraso invalido")', 'raise ValueError(None)'),
    (7, 'raise ValueError("atraso invalido")', 'raise ValueError("XXatraso invalidoXX")'),
    (8, 'raise ValueError("atraso invalido")', 'raise ValueError("ATRASO INVALIDO")'),
    (9, 'if dias <= 5:', 'if dias < 5:'),
    (10, 'if dias <= 5:', 'if dias <= 6:'),
    (11, 'multa = 0', 'multa = None'),
    (12, 'multa = 0', 'multa = 1'),
    (13, 'multa = 0.01 * (dias - 5)', 'multa = None'),
    (14, 'multa = 0.01 * (dias - 5)', 'multa = 0.01 / (dias - 5)'),
    (15, 'multa = 0.01 * (dias - 5)', 'multa = 1.01 * (dias - 5)'),
    (16, 'multa = 0.01 * (dias - 5)', 'multa = 0.01 * (dias + 5)'),
    (17, 'multa = 0.01 * (dias - 5)', 'multa = 0.01 * (dias - 6)'),
    (18, 'total = valor * (1 + multa)', 'total = None'),
    (19, 'total = valor * (1 + multa)', 'total = valor / (1 + multa)'),
    (20, 'total = valor * (1 + multa)', 'total = valor * (1 - multa)'),
    (21, 'total = valor * (1 + multa)', 'total = valor * (2 + multa)'),
    (22, 'return round(total, 2)', 'return round(None, 2)'),
    (23, 'return round(total, 2)', 'return round(total, None)'),
    (24, 'return round(total, 2)', 'return round(2)'),
    (25, 'return round(total, 2)', 'return round(total, )'),
    (26, 'return round(total, 2)', 'return round(total, 3)'),
]


def aplicar(mutantes):
    linhas = list(FONTE)
    for _, velho, novo in mutantes:
        idx = [i for i, l in enumerate(linhas) if l.strip() == velho]
        assert len(idx) == 1, velho
        i = idx[0]
        indent = linhas[i][: len(linhas[i]) - len(linhas[i].lstrip())]
        linhas[i] = indent + novo
    return "\n".join(linhas) + "\n"


def suite_passa(fonte, arq_teste):
    """True se a suite PASSA (= mutante SOBREVIVE)."""
    tmp = Path(tempfile.mkdtemp())
    try:
        (tmp / "multa.py").write_text(fonte)
        (tmp / "tests").mkdir()
        shutil.copy(arq_teste, tmp / "tests")
        env = dict(os.environ, PYTHONPATH=str(tmp))
        r = subprocess.run(
            [sys.executable, "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", "tests"],
            cwd=tmp, env=env, capture_output=True, text=True,
        )
        return r.returncode == 0
    finally:
        shutil.rmtree(tmp)


def experimento(nome_etapa):
    arq = RAIZ / "ex4" / "etapas" / nome_etapa / "test_multa.py"
    # 1a ordem: quais a suite mata?
    mortos = [m for m in MUTANTES if not suite_passa(aplicar([m]), arq)]
    ids_mortos = {m[0] for m in mortos}
    print(f"\n##### Suite {nome_etapa}: mata {len(mortos)} de {len(MUTANTES)} mutantes de 1a ordem")

    pares = [
        (a, b) for a, b in itertools.combinations(mortos, 2) if a[1] != b[1]
    ]  # linhas diferentes
    sobreviventes = [(a, b) for a, b in pares if suite_passa(aplicar([a, b]), arq)]
    print(f"Pares (2 mutantes ja mortos, em linhas diferentes): {len(pares)}")
    print(f"Mutantes de 2a ordem MORTOS    : {len(pares) - len(sobreviventes)}")
    print(f"Mutantes de 2a ordem SOBREVIVEM: {len(sobreviventes)}")
    for a, b in sobreviventes:
        print(f"   sobrevive: mutmut_{a[0]} + mutmut_{b[0]}   [{a[2]}]  +  [{b[2]}]")
    return len(pares), len(sobreviventes)


if __name__ == "__main__":
    for etapa in ("a_bva", "c_final"):
        experimento(etapa)
