""" Crie um programa que utilize o Broadcasting do NumPy para calcular a média de despesas 
    de uma empresa, para cada mês e identificar os meses em que as 
    despesas foram superiores ao dobro da média anual. """

import numpy as np

despesas = np.array([[15000],
                    [12000],
                    [36000],
                    [10000],
                    [18000],
                    [41000],
                    [15000],
                    [11000],
                    [15000],
                    [13000],
                    [13000],
                    [14000]])

media_mensal = []
media_anual = despesas.mean()
media_anual = media_anual

for i, medias in enumerate(despesas):
    if medias > media_anual * 2:
        media_mensal.append(f'O {i+1}° Mês Teve A Média R$ {medias} Que é Maior que o Dobro da Media Anual')
  


print(f'Media Anual R$ {media_anual:.2f}')
print(f'Dobro da Média Anual R$ {media_anual * 2:.2f}')
print(*media_mensal, ' ',sep='\n') 