"""Roda a suíte do ex4 contra os mutantes M10, M17 e M10+M17 (itens d e e).

Uso (dentro de ex4/):  python segunda_ordem/rodar_2a_ordem.py
"""
import pathlib
import shutil
import subprocess
import sys
import tempfile

RAIZ = pathlib.Path(__file__).resolve().parent.parent
ORIG = (RAIZ / "src" / "parcelamento.py").read_text()

VARIANTES = {
    "M10  (n <= 3 -> n <= 4)": [("if n <= 3:", "if n <= 4:")],
    "M17  (n - 3  -> n - 4)": [("(n - 3)", "(n - 4)")],
    "M10 + M17 (2a ordem)": [("if n <= 3:", "if n <= 4:"), ("(n - 3)", "(n - 4)")],
}


def rodar(trocas):
    codigo = ORIG
    for a, b in trocas:
        assert codigo.count(a) == 1
        codigo = codigo.replace(a, b)
    with tempfile.TemporaryDirectory() as d:
        d = pathlib.Path(d)
        (d / "src").mkdir()
        (d / "src" / "parcelamento.py").write_text(codigo)
        shutil.copytree(RAIZ / "tests", d / "tests")
        (d / "pyproject.toml").write_text(
            '[tool.pytest.ini_options]\npythonpath = ["src"]\ntestpaths = ["tests"]\n'
        )
        r = subprocess.run(
            [sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", "-rf"],
            cwd=d, capture_output=True, text=True,
        )
    falhas = [l.split(" - ")[0].replace("FAILED ", "") for l in r.stdout.splitlines() if l.startswith("FAILED")]
    return falhas


for nome, trocas in VARIANTES.items():
    f = rodar(trocas)
    print(f"{nome:28s} -> {'MORTO' if f else 'VIVO '}  testes que falham: {len(f)}")
    for x in f:
        print("      ", x)
