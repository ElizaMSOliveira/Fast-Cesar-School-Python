nome = input('Qual o nome? ')
sexo = input('Qual o Sexo F ou M')
valor = float(input('Qual o valor das compras? '))

if sexo == 'F':
    valor = valor - (valor * 0.13)
else:
    valor = valor - (valor * 0.05)

print('Valor de Sua compra com Desconto R$ {:.2F}'.format(valor))