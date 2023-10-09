from excecoes import NegativeNumberError, SaldoInsuficienteError, ContaInexistenteError
from sua_classe_conta import Conta  # Substitua com o nome real da sua classe Conta
from sua_classe_colecao import ColecaoContas  # Substitua com o nome real da sua classe ColecaoContas
from sua_classe_banco import Banco  # Substitua com o nome real da sua classe Banco

def main():
    colecao = ColecaoContas()
    banco = Banco(colecao)

    while True:
        print("\nEscolha uma opção:")
        print("1. Cadastrar conta")
        print("2. Procurar conta")
        print("3. Realizar depósito")
        print("4. Realizar saque")
        print("0. Sair")

        try:
            escolha = int(input("Opção: "))

            if escolha == 0:
                break
            elif escolha == 1:
                cadastrar_conta(banco)
            elif escolha == 2:
                procurar_conta(banco)
            elif escolha == 3:
                realizar_deposito(banco)
            elif escolha == 4:
                realizar_saque(banco)
            else:
                print("Opção inválida. Tente novamente.")

        except ValueError:
            print("Por favor, insira um número válido.")

def cadastrar_conta(banco):
    try:
        numero = input("Digite o número da conta: ")
        saldo = float(input("Digite o saldo inicial da conta: "))
        conta = Conta(numero, saldo)
        banco.cadastrar_e_procurar_conta(conta)
        print(f"Conta cadastrada com sucesso: {conta.numero}")

    except ValueError:
        print("Por favor, insira um valor numérico válido para o saldo.")

    except ValueError as e:
        print(f"Erro ao cadastrar a conta: {e}")

def procurar_conta(banco):
    numero = input("Digite o número da conta: ")
    try:
        conta = banco.procurar_conta(numero)
        print(f"Conta encontrada: {conta.numero} - Saldo: {conta.saldo}")

    except ContaInexistenteError as e:
        print(f"Erro ao procurar a conta: {e}")

def realizar_deposito(banco):
    numero = input("Digite o número da conta: ")
    try:
        conta = banco.procurar_conta(numero)
        valor_deposito = float(input("Digite o valor do depósito: "))
        conta.deposita(valor_deposito)
        print(f"Depósito realizado com sucesso. Novo saldo: {conta.saldo}")

    except (ContaInexistenteError, NegativeNumberError) as e:
        print(f"Erro ao realizar o depósito: {e}")

def realizar_saque(banco):
    numero = input("Digite o número da conta: ")
    try:
        conta = banco.procurar_conta(numero)
        valor_saque = float(input("Digite o valor do saque: "))
        conta.saca(valor_saque)
        print(f"Saque realizado com sucesso. Novo saldo: {conta.saldo}")

    except (ContaInexistenteError, NegativeNumberError, SaldoInsuficienteError) as e:
        print(f"Erro ao realizar o saque: {e}")

if __name__ == "__main__":
    main()