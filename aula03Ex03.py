
from datetime import date

idade = 0
ano_atual = date.today().year
maior = 0
menor =0

#while x >= 5:
for i in range(5):
    data_nasc = int(input('Dual a data de Nascimento? '))
    #idade = ano_atual - data_nasc

    if ano_atual - data_nasc >= 18:
        maior += 1
    else:
        menor += 1

print('Maior idade {}'.format(maior))
print('Menor Idade {}'.format(menor))



