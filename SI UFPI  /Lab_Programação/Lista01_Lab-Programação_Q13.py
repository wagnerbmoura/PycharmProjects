# calcular redução no tempo de vida
# recebe quantidade de cigarros fumados por dia
# recebe anos de fumo
# perda de 12 minutos de vida por cigarro
# resposta em dias

c = int(input('Informe quantos cigarros fuma por dia: '))
a = int(input('Informe quantos à quantos anos fuma: '))
#1 dia de vida , equivale a 120 cigarros
# número de dias fumando = a*365
# número de cigarros fumados = c*numero de dias fumando
num_c = c*a*365
resp = num_c // 120
print(f'Essa quantidade de cigarros fumados lhe causou uma redução de {resp} dias de vida.')