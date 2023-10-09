from banco import Banco
from excecoes import NegativeNumberError, SaldoInsuficienteError

def main():
    banco = Banco()

    while True:
        print("1. Criar conta")
        print("2. Sacar")
        print("3. Depositar")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            numero = input("Digite o número da conta: ")
            saldo_inicial = float(input("Digite o saldo inicial: "))
            tipo = input("Digite o tipo da conta: ")
            banco.cria_conta(numero, saldo_inicial, tipo)
            print("Conta criada com sucesso!")

        elif opcao == "2":
            numero = input("Digite o número da conta: ")
            valor = float(input("Digite o valor do saque: "))
            try:
                banco.saca(numero, valor)
                print("Saque realizado com sucesso!")
            except NegativeNumberError as e:
                print(str(e))
            except SaldoInsuficienteError as e:
                print(f"Saldo insuficiente para realizar o saque. Valor máximo de saque: {e.valor_maximo_saque}")

        elif opcao == "3":
            numero = input("Digite o número da conta: ")
            valor = float(input("Digite o valor do depósito: "))
            try:
                banco.deposita(numero, valor)
                print("Depósito realizado com sucesso!")
            except NegativeNumberError as e:
                print(str(e))

        elif opcao == "4":
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

        print()

if __name__ == "__main__":
    main()