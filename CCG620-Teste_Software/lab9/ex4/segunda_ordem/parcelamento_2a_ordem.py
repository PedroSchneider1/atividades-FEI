"""Mutante de SEGUNDA ORDEM montado à mão (item d do ex4).

Combina dois mutantes de primeira ordem gerados pelo mutmut, em linhas diferentes:

  M10 (linha 4): if n <= 3:            ->  if n <= 4:
  M17 (linha 7): juros = 0.02*(n - 3)  ->  juros = 0.02*(n - 4)

Os dois "empurram o limite de juros uma parcela para a frente". Quem olha só
a linha 4 ou só a linha 7 vê um erro de uma unidade; juntos parecem coerentes
entre si (começa a cobrar juros uma parcela mais tarde), o que os torna um
bom candidato a mascaramento mútuo.
"""


def parcela(valor, n):
    if n < 1 or n > 12:
        raise ValueError("parcelas invalidas")
    if n <= 4:                      # M10  (original: n <= 3)
        juros = 0
    else:
        juros = 0.02 * (n - 4)      # M17  (original: 0.02 * (n - 3))
    total = valor * (1 + juros)
    return round(total / n, 2)
