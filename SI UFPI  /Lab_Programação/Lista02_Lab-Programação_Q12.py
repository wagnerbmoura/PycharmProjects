d = float(input('Informe o valor da dívida: '))
i = float(input('informe a taxa de juros mensal (em %): '))/100
p = float(input('informe o valor mensal da parcela: '))

di = d
cont = 0
while d > 0:
    d -= p
    d += (d*i)
    cont += 1


print(f'a divida será paga em {cont} meses')
print(f'O total pago será de R${cont * p}')
print(f'O total de juros pagos será de R${(cont * p) - di}')
