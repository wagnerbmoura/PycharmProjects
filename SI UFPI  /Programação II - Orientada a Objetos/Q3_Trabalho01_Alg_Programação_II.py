class Conta:
    _total_contas = 0  # Atributo de classe para contar o total de contas criadas

    __slots__ = ['_numero', '_cliente', '_saldo', '_limite', '_historico']

    def __init__(self, numero, cliente, saldo=0.0, limite=0.0, data_abertura=None):
        Conta._total_contas += 1
        self._numero = numero
        self._cliente = cliente
        self._saldo = saldo
        self._limite = limite
        self._historico = Historico(data_abertura if data_abertura else Data())

    @property
    def numero(self):
        return self._numero

    @property
    def cliente(self):
        return self._cliente

    @property
    def saldo(self):
        return self._saldo

    @property
    def limite(self):
        return self._limite

    @property
    def historico(self):
        return self._historico

    def deposita(self, valor, data=None):
        self._saldo += valor
        self._historico.adiciona_transacao(f"Depósito de R${valor:.2f} na data {data if data else 'indefinida'}")

    def saca(self, valor, data=None):
        if self._saldo >= valor:
            self._saldo -= valor
            self._historico.adiciona_transacao(f"Saque de R${valor:.2f} na data {data if data else 'indefinida'}")
            return True
        else:
            print("Saldo insuficiente.")
            return False

    def transfere_para(self, destino, valor, data=None):
        if self.saca(valor, data):
            destino.deposita(valor, data)
            self._historico.adiciona_transacao(
                f"Transferência de R${valor:.2f} para conta {destino.numero} na data {data if data else 'indefinida'}")
            return True
        else:
            print("Transferência não realizada. Saldo insuficiente.")
            return False

    def extrato(self):
        print(f"Conta número: {self._numero}")
        print(f"Cliente: {self._cliente.nome} {self._cliente.sobrenome}")
        print(f"Saldo atual: R${self._saldo:.2f}")
        self._historico.imprime()

    def calcula_juros(self, taxa, data=None):
        juros = self._limite * (taxa / 100)
        self._saldo -= juros
        self._historico.adiciona_transacao(f"Juros de R${juros:.2f} aplicados na data {data if data else 'indefinida'}")


class Banco:
    def __init__(self):
        self.contas = []

    def cadastro(self, conta):
        self.contas.append(conta)

    def _pesquisa_conta(self, numero):
        for conta in self.contas:
            if conta.numero == numero:
                return conta
        return None

    def deposito(self, numero, valor, data=None):
        conta = self._pesquisa_conta(numero)
        if conta:
            conta.deposita(valor, data)
            return True
        else:
            print("Conta não encontrada.")
            return False

    def saque(self, numero, valor, data=None):
        conta = self._pesquisa_conta(numero)
        if conta:
            return conta.saca(valor, data)
        else:
            print("Conta não encontrada.")
            return False

    def saldo(self, numero):
        conta = self._pesquisa_conta(numero)
        if conta:
            return conta.saldo
        else:
            print("Conta não encontrada.")
            return False

    def transfere(self, origem, destino, valor, data=None):
        conta_origem = self._pesquisa_conta(origem)
        conta_destino = self._pesquisa_conta(destino)

        if conta_origem and conta_destino:
            return conta_origem.transfere_para(conta_destino, valor, data)
        else:
            print("Conta de origem ou destino não encontrada.")
            return False


# Exemplo de uso:
data_abertura_conta = Data(1, 1, 2023)
cliente1 = Cliente("Wagner", "Moura", "123.456.789-01")
cliente2 = Cliente("Marcela", "Lima", "987.654.321-00")

banco = Banco()

conta1 = Conta("001", cliente1, limite=1000.0, data_abertura=data_abertura_conta)
conta2 = Conta("002", cliente2, data_abertura=data_abertura_conta)

banco.cadastro(conta1)
banco.cadastro(conta2)

banco.deposito("001", 500.0, Data(2, 1, 2023))
banco.saque("001", 200.0, Data(3, 1, 2023))
banco.transfere("001", "002", 100.0, Data(4, 1, 2023))

print("Saldo da conta 001:", banco.saldo("001"))
print("Saldo da conta 002:", banco.saldo("002"))


'''Neste exemplo, a classe Banco gerencia uma lista de contas e implementa métodos como cadastro, deposito,
saque, saldo e transfere. A pesquisa de conta é realizada através do método privado _pesquisa_conta.
  O exemplo de uso no final demonstra como criar contas, realizar transações e consultar saldos usando
o banco.'''