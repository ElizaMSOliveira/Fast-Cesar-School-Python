
altura = float(input('Qual a sua ALtura? '))
peso = float(input('Qual o seu peso? '))

imc = peso / altura ** 2
#print(imc)

if 18.5 > imc:
    print('Abaixo do Peso')
elif 18.5 <= imc <= 24.9:
    print('Peso Ideal')
elif 25 <= imc <= 29.9:
    print('Sobrepeso')
elif 30 <= imc <= 39.9:
    print('Obesidade')
else:
    print('Obesidade Morbida')