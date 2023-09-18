cont = 0
cont2 = 0
for i in range(10):
    n = int(input('Digite um valor: '))

    if 10 <= n <= 100:
        cont += 1
    else:
        cont2 += 1

print(f'{cont} números estão dentro do intervalo e {cont2} números não estão.')