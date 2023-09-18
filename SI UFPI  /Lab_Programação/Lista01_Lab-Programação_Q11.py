p = int(input('Informe o preço da mercadoria: '))
d = int(input('Informe o percentual de desconto: '))

print(f'O valor do desconto é de R$ {p*(d/100)}')
print(f'O valor a pagar é R$ {p - (p*(d/100))}')