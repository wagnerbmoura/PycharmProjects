def procurar_letra(f,l):
    list = []
    for i in range(len(f)):
        if f[i] == l:
            list.append(i)
    if len(list) > 0:
        return list
    else:
        return None

#exemplo 1
f = 'uma frase qualquer'
l = 'a'

result = procurar_letra(f,l)
print(result)

#exemplo 2

f = 'testando outra frase'
l = 'm'
result = procurar_letra(f,l)
print(result)