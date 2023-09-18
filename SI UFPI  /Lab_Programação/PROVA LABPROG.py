n1 = int(input('Informe o termo inicial: '))
n2 = int(input('Informe o termo final: '))
ultimo=1
penultimo=1
if (n1==2):
    print("1",'-> ',end='')
if (n1==1):
    print('1', '-> ', end='')
    print('1', '-> ', end='')

for i in range(3,n2+1):
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        if i != (n2):
            print(termo,'-> ',end='')
        if i == (n2):
            print(termo)


