n = int(input('Informe a quantidade de KhW: '))
print(20*'-=')
print( 'Informe o Tipo de instalação:')
print(20*'-=')
print(' R - residências \n I - indústrias \n C - comércios')
e = str(input()).strip().upper()

while e not in 'RIC':
    print('Opção inválida, digite novamente: ')
    e = str(input()).strip().upper()

if e == 'R':
    if n > 750:
        print(f'O preço é R${337.5+((n-750)*0.85)}')
    else:
        print(f'O preço é R${n*0.45}')
elif e == 'I':
    if n > 1200:
        print(f'O preço é R${1140+((n-1200)*1.20)}')
    else:
        print(f'O preço é R${n*0.95}')
elif e == 'C':
    if n > 9000:
        print(f'O preço é R${9450+((n-9000)*1.25)}')
    else:
        print(f'O preço é R${n*1.05}')


