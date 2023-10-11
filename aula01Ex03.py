

carro = int(input('Quantos Carros ele vendeu? '))
vtv = float(input('Qual valor total das vendas? '))
sal = float(input('Qual o Salario fixo? '))
com = float(input('Qual a Comissão recebida por carro? '))

comissao = com * carro
vendaComissao = vtv * 0.05

sal_total = sal + comissao + vendaComissao
print(vtv)
print(comissao)
print(vendaComissao)

print('Vai receber o Salário de R$ {}'.format(sal_total))

