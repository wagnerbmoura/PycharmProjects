class Conta():
    numero = None
    agencia = None
    saldo = 0.0

    def deposita(self,valor):
        self.saldo += valor
    def saque(self,valor):
        self.saldo -= valor

conta1 = Conta()
conta2 = Conta()
conta1.deposita(1000)
conta1.deposita(400)
conta1.saque(300)
conta2.deposita(100)
conta2.saque(50)
conta1.saque(200)
print(conta2.saldo)



