
f_idade18e35 = 0
cast_preto = 0
comum = 0
for i in range(5):

    sexo = input('QUal o Sexo? ')
    olhos = input('Qual a Cor dos Olhos? ')
    cabelos = input('Qual a cor do cabelo? ')
    idade = int(input('Qual a idade?'))

    if sexo == 'f' and  18 <= idade <= 35: #idade >= 18 and idade <=35:
        f_idade18e35 += 1
    if olhos == 'castanhos' and cabelos == 'pretos':
        cast_preto += 1
    else:
        comum += 1
print('Pessoas Femininas entre 18 e 35 anos = {}'.format(f_idade18e35))
print('Olhos Castanhos e Cabelos Pretos = {}'.format(cast_preto))
print('Pessoas Comum = {}'.format(comum))
