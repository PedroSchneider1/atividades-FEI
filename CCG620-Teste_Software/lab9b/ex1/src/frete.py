def modalidade_frete(peso, distancia):
    if peso <= 0 or peso > 30:
        raise ValueError("Peso invalido")
    if distancia < 0 or distancia > 5000:
        raise ValueError("Distancia invalida")
    if peso > 20:
        return "Transportadora"
    if distancia <= 10:
        return "Motoboy"
    elif distancia <= 500:
        return "Correio expresso"
    else:
        return "Correio economico"
