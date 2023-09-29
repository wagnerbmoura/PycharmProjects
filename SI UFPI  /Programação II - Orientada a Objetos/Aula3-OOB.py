class Cliente:
    def __init__(self,cpf,nome,sobrenome):
        self.cpf = cpf
        self.nome = nome
        self.sobrenome = sobrenome
        self.historico = Historico()

class Historico:
    def __init__(self):
        self.transações = []
    def imprime(self):
        print('transações: ')
        for i in self.transações:
            print(f'- {i}')

class Conta:
    def __init__(self,numero,agencia,saldo,cliente):
        self.numero = numero
        self.agencia = agencia
        self.saldo = saldo
        self.titular = cliente
        self.historico = Historico()

    def deposita(self,valor):
        self.saldo += valor
        self.historico.transações.append(f'foi depositato {valor}')

    def saque(self,valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            self.historico.transações.append(f'foi sacado {valor}')
            return True
    def transfere(self,conta_destino,valor):
        self.saldo -= valor
        conta_destino.saldo += valor
        self.historico.transações.append(f'foi transferido {valor}')






cliente1 = Cliente(66990904372,'Wagner','Moura')
conta2 = Conta("1236-5","126-2",100,cliente1)
conta1 = Conta("1234-5","123-2",100,cliente1)

print(conta1.titular.nome)
print(conta1.titular.sobrenome)
print(conta1.titular.cpf)
print(conta1.saldo)
conta1.deposita(10000)
conta1.saque(500)
conta1.deposita(600)
conta1.transfere(conta2,500)
conta1.historico.imprime()
print(conta1.saldo)


''' Nesta aula vimos dois tipos de associação diferente entre objetos, por agregação (onde a existência de um 
 não depende do outro) e por composição  (onde a existencia do objeto depente do outro)
 Enfase para o exemplo de composição com o objeto Historico, adicionado em outros Objetos (Conta e Cliente), 
 onde não há atributos específicos. 
  -->Quando o objeto mãe é usado, O objeto que o compõe será chamado, criando inicialmente uma lista vazia.
  --> Quando o metodo 'imprime' que está dentro do Objeto Historico é chamado mostra-se cada elementendo dessa 
  lista, através de um laço for '''