class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf


class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano


class Historico:
    def __init__(self, data_abertura):
        self.data_abertura = data_abertura
        self.transacoes = []

    def registrar_transacao(self, transacao):
        self.transacoes.append(transacao)

    def imprime(self):
        print(f'Data de abertura da conta: {self.data_abertura.dia}/{self.data_abertura.mes}/{self.data_abertura.ano}')
        for transacao in self.transacoes:
            print(transacao)


class Conta:
    def __init__(self, numero, cliente, limite=0.0):
        self.numero = numero
        self.saldo = 0.0
        self.limite = limite
        self.cliente = cliente
        self.historico = Historico(Data(1, 1, 2022))

    def deposita(self, valor, data=None):
        if valor > 0:
            self.saldo += valor
            transacao = f'{data.dia}/{data.mes}/{data.ano} - Depósito: R$ {valor:.2f}'
            self.historico.registrar_transacao(transacao)
            return True
        return False

    def saca(self, valor, data=None):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
            self.limite -= (self.limite + self.saldo)
            self.saldo = 0
            transacao = f'{data.dia}/{data.mes}/{data.ano} - Saque: R$ {valor:.2f}'
            self.historico.registrar_transacao(transacao)
            return True
        return False

    def transfere_para(self, destino, valor, data=None):
        if valor <= self.saldo + self.limite:
            destino.deposita(valor, data)
            transacao = f'{data.dia}/{data.mes}/{data.ano} - Transferência para conta {destino.numero}: R$ {valor:.2f}'
            self.historico.registrar_transacao(transacao)
            return True
        return False

    def extrato(self):
        print(f'Número da conta: {self.numero}')
        print(f'Cliente: {self.cliente.nome} {self.cliente.sobrenome}')
        print(f'Saldo: R$ {self.saldo:.2f}')
        print(f'Limite: R$ {self.limite:.2f}')
        self.historico.imprime()

    def calcula_juros(self, taxa, data=None):
        juros = (self.saldo + abs(self.limite)) * (taxa / 100)
        self.saldo -= juros
        transacao = f'{data.dia}/{data.mes}/{data.ano} - Cálculo de juros: R$ {juros:.2f}'
        self.historico.registrar_transacao(transacao)

'''EXEMPLOS: '''

cliente1 = Cliente("Wagner", "Moura", "123456789")
conta1 = Conta("0123456", cliente1, limite=5000)
conta2 = Conta("0123457",cliente1,limite=3000)

data_deposito = Data(10, 3, 2022)
conta1.deposita(1000, data_deposito)

data_saque = Data(15, 3, 2022)
conta1.saca(3000, data_saque)

data_transferencia = Data(1, 10,2023)

conta1.extrato()

'''Isso irá criar um cliente chamado Wagner Moura, com CPF 123456789, e uma conta com número "0123456"
e limite de R$ 5000. Em seguida, é realizada uma operação de depósito no valor de R$ 1000 em 10/03/2022,
seguida por um saque de R$ 3000 em 15/03/2022, em seguida uma transferencia de R$2000 em 1/10/2023 para conta de mesmo cliente.
Por fim, o extrato da conta será impresso com todas as transações registradas.'''


