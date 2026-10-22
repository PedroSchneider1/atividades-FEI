from itertools import product

NOMES = ("cartao", "documento", "grupo_chamado", "prioridade")


def regra(cartao, documento, grupo_chamado, prioridade):
    """Especificação: embarca se (cartão E documento E grupo chamado) OU prioridade."""
    return bool((cartao and documento and grupo_chamado) or prioridade)


def pares_independentes(decisao, n):
    """
    Para cada condição i, devolve os pares (a, b) de linhas da tabela-verdade
    que diferem apenas em i e para os quais a decisão muda.
    Retorna dict {i: [(a, b), ...]}.
    """
    linhas = list(product((False, True), repeat=n))
    resultado = {}
    for i in range(n):
        pares = []
        for a in linhas:
            if a[i]:
                continue  # cada par é considerado uma vez (i = False em a)
            b = a[:i] + (True,) + a[i + 1:]
            if bool(decisao(*a)) != bool(decisao(*b)):
                pares.append((a, b))
        resultado[i] = pares
    return resultado

print(pares_independentes(regra, 4))
