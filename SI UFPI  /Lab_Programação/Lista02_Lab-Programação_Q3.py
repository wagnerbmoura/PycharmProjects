l = []
resp = ''
for i in range(3):
    n = int(input('Digite um valor: '))
    l.append(n)
if l[0] < (l[1] + l[2]) and l[1] < (l[0] + l[2]) and l[2] < (l[0] + l[1]):
    resp = 'sim'
else:
    print('Os segmentos informados não formam um triângulo')

l2 = []
if resp == 'sim':
    for i in l:
        if i not in l2:
            l2.append(i)

if len(l2) == 1:
    print('O triangulo formado pelos lados informados é equilátero')
if len(l2) == 2:
    print('O triangulo formado pelos lados informados é isósceles')
if len(l2) == 3:
    print('O triangulo formado pelos lados informados é escaleno')







