def classificar_estoque(quantidade: int) -> str:
    if quantidade >= 100:
        return "Alto"
    elif quantidade >= 20:
        return "Normal"
    else:
        return "Baixo"
