print(20*'-=')
print('Informe o código do produto: ')
n = str(input()).lower().strip()
d = {'a':'PAPEL','b':'CANETA','c':'LÁPIS','d':'BORRACHA'}

if n in d.keys():
    for c in d.keys():
        if c == n:
            print(d[c])
else:
    print('Não encontrado')

