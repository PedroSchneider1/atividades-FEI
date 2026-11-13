def menor_preco(precos):
    if not precos:
        raise ValueError("sem cotacoes")
    m = precos[0]
    for p in precos[1:]:
        if p < m:
            m = p
    return m


def dia_da_compra(precos):
    if not precos:
        raise ValueError("sem cotacoes")
    pos = 0
    for i in range(1, len(precos)):
        if precos[i] <= precos[pos]:
            pos = i
    return pos
