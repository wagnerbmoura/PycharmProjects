from statistics import mean
l = []
n = int
n = int(input('Digite um número: '))
while n != 0:
    l.append(n)
    n = int(input('Digite outro número: '))

print(f'você digitou {len(l)} números')
if len(l) >= 1:
    print(f'A média dos números digitados é {mean(l):.2f}')


