def forca(senha):
    if len(senha) < 8:
        return "fraca"
    pontos = 0
    for c in senha:
        if c.isdigit():
            pontos += 1
        elif not c.isalnum():
            pontos += 2
    if pontos >= 4:
        return "forte"
    return "media"
