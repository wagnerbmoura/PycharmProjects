d = {'a':1.45,'b':1.15,'c':1.25,'d':1.10,'e':1.90,'f':1.60,'outros':1.05}
while True:
    p = int(input('Informe o preço: '))
    c = str(input('informe a categoria: ')).lower().strip()
    for chave in d.keys():
        if chave == c:
            print(f'O preço preço reajustado é de {p*d[chave]}')
            s = str(input('Quer continuar?(S/N): ')).lower().strip()
    if s in 'não,n':
        print('programa finalizado')
        break

