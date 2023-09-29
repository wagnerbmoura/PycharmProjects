class Conta:
    def __init__(self,numero,agencia,saldo):
        self._numero = numero
        self._agencia = agencia
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self,saldo):
        if saldo < 0:
            print('Não pode ser negativo')
        else:
            self.saldo = saldo

    '''def get_saldo(self):
        return self._saldo

    def set_saldo(self,novo_saldo):
        self._saldo = novo_saldo'''

    def deposita(self,valor):
        self._saldo += valor

    def saque(self,valor):
        if self._saldo < valor:
            return False
        else:
            self._saldo -= valor
            return True

    def transfere(self,conta_destino,valor):
        self._saldo -= valor
        conta_destino.saldo += valor
        return True

conta2 = Conta("1236-5","126-2",100)
conta1 = Conta("1234-5","123-2",100)

conta1.deposita(200)
'''conta1.saldo = 500
conta1.__saldo = 400'''

# diferenças entre atributos publico, protegido, e privado
# métodos de proteção

conta1.deposita(1000)
print(conta1.saldo)



