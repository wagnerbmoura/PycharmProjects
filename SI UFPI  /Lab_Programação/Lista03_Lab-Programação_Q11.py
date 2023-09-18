def string_na_lista(s,l):
    resp = ''
    for i in l:
        if s == i:
            resp = 'verdadeiro'
            break
        else:
            resp = 'falso'
    return resp

# Exemplo 1
s = 'macaco'
l = ['jacaré','macaco','hipopótamo','lagartixa']

result = string_na_lista(s,l)
print(result)

# Exemplo 2
s = 'pato'
l = ['jacaré','macaco','hipopótamo','lagartixa']

result = string_na_lista(s,l)
print(result)
