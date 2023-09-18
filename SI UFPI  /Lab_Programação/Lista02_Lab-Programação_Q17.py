l = []
l2 = []
l3 = []
for i in range(10):
    n = int(input('Digite um número: '))
    if i%2 == 0:
        l.append(n)
        l3.append(n)
    else:
        l2.append(n)
        l3.append(n)
print(l)
print(l2)
print(l3)
