def mdc(n1,n2):
    count = 0
    for i in range(1,n1+1):
        if n1%i == 0 and n2%i == 0:
            count = i
    return count

#Exemplo 1
n1 = 36
n2 = 12
result = mdc(n1,n2)
print(result)
