l = []
for i in range(10):
    n = int(input('Digite o número: '))
    l.append(n)

l.sort()
print(l)
l.sort(reverse=True)
print(l)


