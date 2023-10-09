class NegativeNumberError(Exception):
    pass

class SaldoInsuficienteError(Exception):
    pass

class Conta:
    def __init__(self, numero: str, saldo: float):
        self._numero = numero
        self._saldo = saldo

    def get_numero(self) -> str:
        return self._numero

    def get_saldo(self) -> float:
        return self._saldo

    def deposita(self, valor: float):
        if valor < 0:
            raise NegativeNumberError("O valor do depósito não pode ser negativo.")
        self._saldo += valor

    def saca(self, valor: float):
        if valor < 0:
            raise NegativeNumberError("O valor do saque não pode ser negativo.")
        if valor > self._saldo:
            raise SaldoInsuficienteError("Saldo insuficiente para realizar o saque.")
        self._saldo -= valor


