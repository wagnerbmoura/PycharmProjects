def Valor_Pagamento(p,a):
    if a == 0:
        return f'O valor a ser pago é {p}'
    if a != 0:
        p = (p*1.03)
        for i in range(a):
            p += (p*0.01)
        return p


#Exemplo
p = 100
a = 5
result = Valor_Pagamento(p,a)
print(result)