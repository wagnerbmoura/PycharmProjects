a = int(input('Digite o ano para verificar: '))
if a%400 == 0 or (a%4 == 0 and a%100 != 0):
    print('É bissexto')
else:
    print('Não é bissexto')