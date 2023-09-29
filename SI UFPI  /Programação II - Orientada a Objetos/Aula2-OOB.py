class Conta:
    def __init__(self,numero,agencia,saldo):
        self.numero = numero
        self.agencia = agencia
        self.saldo = saldo

    def deposita(self,valor):
        self.saldo += valor
    def saque(self,valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True
    def transfere(self,conta_destino,valor):
        self.saldo -= valor
        conta_destino.saldo += valor


conta1 = Conta("1234-5","123-2",100)
conta2 = Conta('1235-5','124-2',0)
print(conta1.saldo)

conta1.deposita(400)
conta1.saque(100)
conta1.deposita(900)

print(conta1.saldo)
print(conta2.saldo)

conta1.transfere(conta2,300)
print(conta2.saldo)

'''Nesta aula declaramos a classe novamente , mas usamos o método init para iniciar a função automaticamente
já com valores passados na criação do Objeto, tambem testamos o chamamento de outros métodos pelos objetos criados'''