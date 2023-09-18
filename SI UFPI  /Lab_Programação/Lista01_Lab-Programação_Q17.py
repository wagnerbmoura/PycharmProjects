ci = 0
for i in range(4):
    n = int(input('Digite um número: '))
    if n%2 != 0:
        ci += n
print(ci)