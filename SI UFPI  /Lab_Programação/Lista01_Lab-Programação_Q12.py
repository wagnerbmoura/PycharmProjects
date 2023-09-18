print(20*'*')
print('Aluguel de Carros: ')
print(20*'*')
d = int(input('Quantos dias o carro foi alugado ?: '))
k = int(input('Quantos km foram percorridos ?: '))
vd = 95 * d
vk = 0.18 * k
print(20*'*')
print(f'O valor total a pagar é de R${vd+vk}')
