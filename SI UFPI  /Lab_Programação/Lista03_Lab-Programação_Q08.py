def converte_temp(F):
    C = (F-32)*(5/9)
    return C

F = 56

r = converte_temp(F)
print(r)