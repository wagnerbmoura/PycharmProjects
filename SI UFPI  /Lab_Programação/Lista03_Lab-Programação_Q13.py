def divisores(n):
    l = []
    for i in range(1,n+1):
        if n%i == 0:
            l.append(i)
    print(l)
    if len(l) == 2:
        return 'É primo'
    else:
        return 'Não é primo'

# Exemplo 1
n = 10
result = divisores(n)
print(result)

# Exemplo 2
n = 5
result = divisores(n)
print(result)

