"""
Evidencia EMPIRICA de equivalencia (nao e uma prova formal!).

Compara a funcao original com cada mutante em TODAS as listas de
tamanho 1 a 6 com valores de 0 a 3. Se nunca ha diferenca, o mutante
e (muito provavelmente) equivalente; se ha, mostramos um contra-exemplo.

Rodar:  python ex3/extras/equivalencia_forca_bruta.py
"""
from itertools import product


# ---------------- ORIGINAIS ----------------
def menor_preco(precos):
    m = precos[0]
    for p in precos[1:]:
        if p < m:
            m = p
    return m


def dia_da_compra(precos):
    pos = 0
    for i in range(1, len(precos)):
        if precos[i] <= precos[pos]:
            pos = i
    return pos


# ---------------- MUTANTES ----------------
def menor_preco_mut8(precos):          # p < m  ->  p <= m
    m = precos[0]
    for p in precos[1:]:
        if p <= m:
            m = p
    return m


def menor_preco_mut7(precos):          # precos[1:] -> precos[2:]
    m = precos[0]
    for p in precos[2:]:
        if p < m:
            m = p
    return m


def dia_mut9(precos):                  # range(1, n) -> range(n)
    pos = 0
    for i in range(len(precos)):
        if precos[i] <= precos[pos]:
            pos = i
    return pos


def dia_mut11(precos):                 # range(1, n) -> range(2, n)
    pos = 0
    for i in range(2, len(precos)):
        if precos[i] <= precos[pos]:
            pos = i
    return pos


def dia_mut12(precos):                 # <= -> <
    pos = 0
    for i in range(1, len(precos)):
        if precos[i] < precos[pos]:
            pos = i
    return pos


CASOS = [
    ("menor_preco  mutmut_8  (p < m -> p <= m)", menor_preco, menor_preco_mut8),
    ("menor_preco  mutmut_7  (precos[1:] -> precos[2:])", menor_preco, menor_preco_mut7),
    ("dia_da_compra mutmut_9  (range(1,n) -> range(n))", dia_da_compra, dia_mut9),
    ("dia_da_compra mutmut_11 (range(1,n) -> range(2,n))", dia_da_compra, dia_mut11),
    ("dia_da_compra mutmut_12 (<= -> <)", dia_da_compra, dia_mut12),
]

for nome, orig, mut in CASOS:
    total = 0
    contra = None
    for n in range(1, 7):
        for lista in product(range(4), repeat=n):
            lista = list(lista)
            total += 1
            if orig(lista) != mut(lista) and contra is None:
                contra = (lista, orig(lista), mut(lista))
    if contra is None:
        print(f"EQUIVALENTE?  {nome}\n    -> {total} listas testadas, nenhuma diferenca.\n")
    else:
        lista, o, m = contra
        print(f"NAO EQUIVALENTE  {nome}\n    -> contra-exemplo: {lista}  original={o}  mutante={m}\n")
