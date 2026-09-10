def retirar_do_estoque(estoque_atual: int, quantidade: int) -> int:
    if quantidade > estoque_atual:
        raise ValueError("Quantidade insuficiente em estoque")
    return estoque_atual-quantidade
