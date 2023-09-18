ímpares = []
pares = []

for i in range(10,101):
    if 10 <= i <= 50:
        if i%2 != 0:
            ímpares.append(i)
    if 51 <= i <= 100:
        if i%2 == 0:
            pares.append(i)

print(ímpares)
print(pares)