def verificar(v):
    c = v[:]
    c.sort()
    if v == c:
        return True
    else:
        return None

#Exemplo 1
v = [0,2,4,5,6,7,8,23,54,65]
result = verificar(v)
print(result)

#Exemplo 2
v = [0,2,5,4,6,7,23,8,54,65]
result = verificar(v)
print(result)

#Exemplo 3
v = [0,1,2,3,4,5,6,7,8,9]
result = verificar(v)
print(result)
