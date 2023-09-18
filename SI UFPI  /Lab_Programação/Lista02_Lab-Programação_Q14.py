print(20*'-=')
print(f"{'TABUADA':^30}")
print(20*'-=')
e = int
n = int(input('Digite um número: '))
while e != 5:
    print('Escolha uma opção:\n 1-ADIÇÃO \n 2-SUBTRAÇÃO \n 3-DIVISÃO \n 4-MULTIPLICAÇÃO \n 5-SAIR ')
    e = int(input())
    for i in range(1,10):
        if e == 1:
            print(f'{e}+{i}={e+i:.1f}')
        if e == 2:
            print(f'{e}-{i}={e - i:.1f}')
        if e == 3:
            print(f'{e}÷{i}={e / i:.1f}')
        if e == 4:
            print(f'{e}X{i}={e * i:.1f}')
print('Programa finalizado')
