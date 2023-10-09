from colecaocontas import ColecaoContas
from conta import Conta, NegativeNumberError, SaldoInsuficienteError

class Banco:
    def __init__(self):
        self._repositorio_contas = ColecaoContas()

    def cria_conta(self, numero, saldo_inicial, tipo):
        conta = Conta(numero, saldo_inicial)
        self._repositorio_contas.cadastra_conta(conta)

    def saca(self, numero, valor):
        conta = self._repositorio_contas.procura_conta(numero)
        try:
            conta.saca(valor)
        except NegativeNumberError as e:
            print(str(e))
        except SaldoInsuficienteError as e:
            print(str(e))

    def deposita(self, numero, valor):
        conta = self._repositorio_contas.procura_conta(numero)
        try:
            conta.deposita(valor)
        except NegativeNumberError as e:
            print(str(e))
