sm = float(input('Digite o Salario do Funcionario: '))
bonus = sm * 0.10
sf = sm + bonus

print('O Salário inicial é {:.2f}\nO Salário Final é {:.2f}\nO Acrescimo foi de R${:.2f}'.format(sm, sf, bonus))