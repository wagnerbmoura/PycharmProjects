p_a = 6000000
t_a = 0.055
p_b = 10000000
t_b = 0.032

cont = 0
while p_a <= p_b:
    p_a += (p_a * t_a)
    p_b += (p_b * t_b)
    cont += 1

print(f'Nestes ritmos de crescimento, levará um total de {cont} anos, para a população de cidade A ultrapassar a da cidade B')