def valor_com_multa(valor, dias):
    if dias < 0 or dias > 60:
        raise ValueError("atraso invalido")
    if dias <= 5:
        multa = 0
    else:
        multa = 0.01 * (dias - 5)
    total = valor * (1 + multa)
    return round(total, 2)
