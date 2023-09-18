d = {0:'zero',1:'um',2:'dois',3:'três',4:'quatro',5:'cinco',6:'seis',7:'sete',8:'oito',9:'nove',10:'dez',11:'onze',12:'doze',13:'treze',14:'quatorze',15:'quinze',16:'dezeseis',17:'dezessete',18:'dezoito',19:'dezenove',20:'vinte'}
n = int(input('Digite o número: '))

if 0 <= n <= 20:
    print(d[n])
else:
    print('número inválido')