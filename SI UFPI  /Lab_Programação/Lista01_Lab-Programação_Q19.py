k = int(input('Quantos quilometros vocẽ quer percorrer?: '))
if k <= 250:
    print(f'O custo da viagem é de R$ {k*0.65}')
if k > 250:
    print(f'O custo da viagem é de R$ {k*0.35}')