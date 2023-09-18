n = str(input('Digite qualquer coisa: ')).strip()
t = ''
t2 = ''
for i in n:
    if i != ' ':
        t += i
for i in t:
    if i not in t2:
        t2 += i
        print(f'O caracter {i} aparece {t.count(i)} vezes')
