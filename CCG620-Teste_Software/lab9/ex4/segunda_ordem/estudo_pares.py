"""Estudo de mutantes de SEGUNDA ORDEM do ex4 (itens d e e).

Para cada par de mutantes de primeira ordem em linhas DIFERENTES do codigo
(2 mutacoes na mesma linha nao se combinam), aplica as duas mudancas ao
mesmo tempo, roda a suite do ex4 contra o resultado e conta se o mutante
de segunda ordem foi morto.

Uso (dentro de ex4/):  python segunda_ordem/estudo_pares.py
Os 27 mutantes abaixo sao exatamente os gerados pelo mutmut 3.8.0
(numeracao = parcelamento.x_parcela__mutmut_N).
"""
import itertools
import pathlib
import shutil
import subprocess
import sys
import tempfile

RAIZ = pathlib.Path(__file__).resolve().parent.parent
FONTE = (RAIZ / "src" / "parcelamento.py").read_text().splitlines()

MUTANTES = [
    (1, 'if n < 1 or n > 12:', 'if n < 1 and n > 12:'),
    (2, 'if n < 1 or n > 12:', 'if n <= 1 or n > 12:'),
    (3, 'if n < 1 or n > 12:', 'if n < 2 or n > 12:'),
    (4, 'if n < 1 or n > 12:', 'if n < 1 or n >= 12:'),
    (5, 'if n < 1 or n > 12:', 'if n < 1 or n > 13:'),
    (6, 'raise ValueError("parcelas invalidas")', 'raise ValueError(None)'),
    (7, 'raise ValueError("parcelas invalidas")', 'raise ValueError("XXparcelas invalidasXX")'),
    (8, 'raise ValueError("parcelas invalidas")', 'raise ValueError("PARCELAS INVALIDAS")'),
    (9, 'if n <= 3:', 'if n < 3:'),
    (10, 'if n <= 3:', 'if n <= 4:'),
    (11, 'juros = 0', 'juros = None'),
    (12, 'juros = 0', 'juros = 1'),
    (13, 'juros = 0.02 * (n - 3)', 'juros = None'),
    (14, 'juros = 0.02 * (n - 3)', 'juros = 0.02 / (n - 3)'),
    (15, 'juros = 0.02 * (n - 3)', 'juros = 1.02 * (n - 3)'),
    (16, 'juros = 0.02 * (n - 3)', 'juros = 0.02 * (n + 3)'),
    (17, 'juros = 0.02 * (n - 3)', 'juros = 0.02 * (n - 4)'),
    (18, 'total = valor * (1 + juros)', 'total = None'),
    (19, 'total = valor * (1 + juros)', 'total = valor / (1 + juros)'),
    (20, 'total = valor * (1 + juros)', 'total = valor * (1 - juros)'),
    (21, 'total = valor * (1 + juros)', 'total = valor * (2 + juros)'),
    (22, 'return round(total / n, 2)', 'return round(None, 2)'),
    (23, 'return round(total / n, 2)', 'return round(total / n, None)'),
    (24, 'return round(total / n, 2)', 'return round(2)'),
    (25, 'return round(total / n, 2)', 'return round(total / n, )'),
    (26, 'return round(total / n, 2)', 'return round(total * n, 2)'),
    (27, 'return round(total / n, 2)', 'return round(total / n, 3)'),
]

EQUIVALENTES = {9}  # n <= 3 -> n < 3


def aplicar(muts):
    linhas = list(FONTE)
    for _, antigo, novo in muts:
        idx = [k for k, l in enumerate(linhas) if l.strip() == antigo]
        assert len(idx) == 1, antigo
        k = idx[0]
        indent = linhas[k][: len(linhas[k]) - len(linhas[k].lstrip())]
        linhas[k] = indent + novo
    return "\n".join(linhas) + "\n"


def suite_passa(codigo):
    with tempfile.TemporaryDirectory() as d:
        d = pathlib.Path(d)
        (d / "src").mkdir()
        (d / "src" / "parcelamento.py").write_text(codigo)
        shutil.copytree(RAIZ / "tests", d / "tests")
        (d / "pyproject.toml").write_text(
            '[tool.pytest.ini_options]\npythonpath = ["src"]\ntestpaths = ["tests"]\n'
        )
        r = subprocess.run(
            [sys.executable, "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider"],
            cwd=d, capture_output=True, text=True,
        )
        return r.returncode == 0  # True = suite NAO detectou (mutante vivo)


if __name__ == "__main__":
    total = mortos = 0
    vivos = []
    for a, b in itertools.combinations(MUTANTES, 2):
        if a[1] == b[1]:  # mesma linha de codigo
            continue
        total += 1
        if suite_passa(aplicar([a, b])):
            vivos.append((a[0], b[0]))
        else:
            mortos += 1
    print(f"pares de 2a ordem testados: {total}")
    print(f"mortos: {mortos}   vivos: {len(vivos)}")
    nao_equiv = [p for p in vivos if not (set(p) & EQUIVALENTES)]
    print("vivos que envolvem o equivalente #9:", [p for p in vivos if set(p) & EQUIVALENTES])
    print("vivos SEM o equivalente:", nao_equiv)
