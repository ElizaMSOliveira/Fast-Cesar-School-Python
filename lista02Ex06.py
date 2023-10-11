
num = float(input('Digite um numero: '))


if 0 <= num <= 25:
    print('Numero entre [0 , 25]')
elif 25 < num <= 50:
    print('Numero entre [25 , 50]')
elif 50 < num <= 75:
    print('Número entre [50 , 75]')
elif 75 < num <= 100:
    print('Número entre [75 , 100]')
else:
    print('Número Fora de Intervalo')
