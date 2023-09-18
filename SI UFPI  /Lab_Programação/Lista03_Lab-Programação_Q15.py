def ver_hora(s):
    count = 0
    for i in range(len(s)):
        if i in [0,1,3,4,6,7] and s[i].isdigit() == True:
            count += 1
        if i in [2,5] and s[i] == ':':
            count += 1
    if count == 8:
        return 'O formato está correto'
    else:
        return 'O formato está errado'

#Exemplo 1
s = '04:05:30'
result = ver_hora(s)
print(result)

#Exemplo 2
s = '05/04/23'
result = ver_hora(s)
print(result)
