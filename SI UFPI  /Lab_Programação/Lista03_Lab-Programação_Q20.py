def nascimento(i):
    "A função calcula o ano de nascimento"
    from datetime import date
    d = date.today().year
    r = d-i
    return f'O ano de nascimento é {r}'

#Exemplo 1
i = 35
result = nascimento(i)
print(result)