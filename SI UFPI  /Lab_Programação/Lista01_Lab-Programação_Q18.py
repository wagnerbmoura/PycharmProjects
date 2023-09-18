s = int(input('Qual o valor do seu salário?: '))
if s > 2500:
    print(f'Você recebeu um aumento, seu novo salário é de R$ {s+(0.07*s)}')
elif s <= 2500:
    print(f'Você recebeu um aumento, seu novo salário é de R$ {s+(0.1 * s)}')
