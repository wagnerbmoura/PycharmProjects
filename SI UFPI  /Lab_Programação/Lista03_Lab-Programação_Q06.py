def contar_caracteres(frase):
    count = 0
    for i in frase:
        if i != ' ':
            count += 1
    return count


result = contar_caracteres('wagner braga moura')
print(result)