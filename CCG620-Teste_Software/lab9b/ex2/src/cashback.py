def cashback(compras):
    total = 0
    for valor in compras:
        if valor >= 100:
            total += valor * 0.05
    return round(total, 2)
