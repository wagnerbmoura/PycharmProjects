class NegativeNumberError(Exception):
    pass

class SaldoInsuficienteError(Exception):
    def __init__(self, mensagem, valor_maximo_saque):
        super().__init__(mensagem)
        self.valor_maximo_saque = valor_maximo_saque