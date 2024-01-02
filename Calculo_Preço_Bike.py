l = 'quadro 1200 , pedais 200 , rodas 2000 , pneus 600 , camaras de ar tpu 200 , grupo slx com pedevela gxp 3500 , guidão crankbrothers R$200 , canote crankbrothers 360 , selim fzik 900 , abraçadeira de canote 70 , manoplas 100 , freio hidraulico 300 , caixa de direção integrada 100, suspensão absolute 800'
s = 0
for i in l.split():
    if i.isnumeric():
        s += (int(i))

print(s)





