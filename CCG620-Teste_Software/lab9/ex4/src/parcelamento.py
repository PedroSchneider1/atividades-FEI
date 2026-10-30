def parcela(valor, n):
    if n < 1 or n > 12:
        raise ValueError("parcelas invalidas")
    if n <= 3:
        juros = 0
    else:
        juros = 0.02 * (n - 3)
    total = valor * (1 + juros)
    return round(total / n, 2)
