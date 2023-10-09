from repositoriocontas import RepositorioContas

class ContaInexistenteError(Exception):
    pass

class ColecaoContas(RepositorioContas):
    def __init__(self):
        self._contas = {}

    def cadastra_conta(self, conta):
        numero = conta.get_numero()
        if numero in self._contas:
            raise ValueError("Já existe uma conta com o número fornecido.")
        self._contas[numero] = conta

    def procura_conta(self, numero):
        if numero not in self._contas:
            raise ContaInexistenteError("A conta com o número fornecido não existe.")
        return self._contas[numero]