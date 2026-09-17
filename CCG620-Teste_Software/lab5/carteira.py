class SaldoInsuficienteError(Exception):
    """Levantada quando se tenta sacar um valor maior que o saldo disponível."""
    pass


class CarteiraDigital:
    def __init__(self, saldo_inicial=0, log_path="carteira.log"):
        self.saldo = saldo_inicial
        self.log_path = log_path

    def depositar(self, valor):
        self.saldo += valor
        with open(self.log_path, "a") as f:
            f.write(f"deposito:{valor}\n")

    def sacar(self, valor):
        if valor > self.saldo:
            raise SaldoInsuficienteError("saldo insuficiente")
        self.saldo -= valor


def classificar_transacao(valor):
    """
    Regras (limites inclusivos na categoria de cima):
        valor < 100             -> "pequena"
        100 <= valor < 1000     -> "media"
        valor >= 1000           -> "grande"
    """
    if valor < 100:
        return "pequena"
    elif valor < 1000:
        return "media"
    else:
        return "grande"


def transferir(origem, destino, valor):
    origem.sacar(valor)
    destino.depositar(valor)
