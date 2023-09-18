v = int(input('Informe a velocidade do carro(km/h): '))
if v > 90:
    m = (v-90)*6.75
    print(f'Velocidade acima do permitido, você foi multado em R$ {m}')
