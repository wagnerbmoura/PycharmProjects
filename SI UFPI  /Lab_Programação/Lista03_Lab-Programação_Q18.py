def div_2_3(v):
    l = []
    for i in v:
        if i%2 == 0 and i%3 == 0:
            l.append(i)
    return l


#Exemplo
v = [12,3,4,34,54,65,76,34,25]
result = div_2_3(v)
print(result)
