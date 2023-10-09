#OBSERVAÇÃO: neste está apenas o código da alteração, irá dar erro pelas classes faltantes.

class Conta:
    _total_contas = 0

    __slots__ = ['_numero', '_saldo', '_limite', '_cliente', '_historico']

    def __init__(self, cliente, limite=0.0):
        Conta._total_contas += 1
        self._numero = self._gerar_numero_conta()
        self._saldo = 0.0
        self._limite = limite
        self._cliente = cliente
        self._historico = Historico(Data(1, 1, 2022))

    @property
    def numero(self):
        return self._numero

    @property
    def saldo(self):
        return self._saldo

    @property
    def limite(self):
        return self._limite

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    @staticmethod
    def _gerar_numero_conta():
        return str(Conta._total_contas).zfill(6)

    def deposita(self, valor, data=None):
        if valor > 0:
            self._saldo += valor
            transacao = f'{data.dia}/{data.mes}/{data.ano} - Depósito: R$ {valor:.2f}'
            self._historico.registrar_transacao(transacao)
            return True
        return False

    def saca(self, valor, data=None):
        if valor <= self._saldo + self._limite:
            self._saldo -= valor
            transacao = f'{data.dia}/{data.mes}/{data.ano} - Saque: R$ {valor:.2f}'
            self._historico.registrar_transacao(transacao)
            return True
        return False

    def transfere_para(self, destino, valor, data=None):
        if self.saca(valor, data):
            destino.deposita(valor, data)
            transacao = f'{data.dia}/{data.mes}/{data.ano} - Transferência para conta {destino.numero}:R$ {valor:.2f}'
            self._historico.registrar_transacao(transacao)
            return True
        return False

    def extrato(self):
        print(f'Número da conta: {self._numero}')
        print(f'Cliente: {self._cliente.nome} {self._cliente.sobrenome}')
        print(f'Saldo: R$ {self._saldo:.2f}')
        print(f'Limite: R$ {self._limite:.2f}')
        self._historico.imprime()

    def calcula_juros(self, taxa, data=None):
        juros = (self._saldo + abs(self._limite)) * (taxa / 100)
        self._saldo -= juros
        transacao = f'{data.dia}/{data.mes}/{data.ano} - Cálculo de juros: R$ {juros:.2f}'
        self._historico.registrar_transacao(transacao)

'''     Nessa nova versão,foi usado o atributo de classe `_total_contas` para gerar automaticamente o número 
da conta. A cada inicialização de um objeto da classe Conta, incrementamos o valor desse atributo e formatamos 
o número da conta utilizando `zfill(6)` para preencher com zeros à esquerda.
        Além disso, utilizamos o decorador `@property` para criar propriedades somente leitura para os atributos, 
protegendo-os contra alterações diretas fora da classe. E utilizamos `__slots__` para evitar que sejam criados 
atributos dinâmicos além dos especificados na lista.
        Dessa forma, podemos criar objetos da classe Conta normalmente e acessar os atributos de maneira segura:  '''

#EXEMPLOS:
cliente1 = Cliente("Wagner", "Wagner", "123456789")
conta1 = Conta(cliente1, limite=5000)

data_deposito = Data(10, 3, 2022)
conta1.deposita(1000, data_deposito)

data_saque = Data(15, 3, 2022)
conta1.saca(500, data_saque)

conta1.extrato()