"""Crie um programa que utilize o NumPy para calcular a média de vendas nos primeiros 10 dias
 e verificar se houve algum dia em que as vendas foram maiores que 1000. """

import numpy as np

vendas = np.array([[2000,500,100],
                  [300,4000,800],
                  [50,60,800],
                  [350,6000,50],
                  [2000,200,200],
                  [320,6500,2210],
                  [8000,700,100],
                  [5000,250,360],
                  [1500,2800,190],
                  [500,600,1000],
                  [250,450,8000],
                  [400,600,120]])

media = []
vendas_maiores = []

for medias in vendas[0:10]:
    media.append(medias.mean())
    #media_maior_7.append(f'O Aluno Na {i+1}° Posição Obteve a Nota {maior}')

for i, maiores in enumerate(media):
    if maiores > 1000:
        vendas_maiores.append(f'O {i+1}° dia Teve a media de Venda em R$ {maiores:.2f}')

print('*** MÉDIAS ***')
print(*media, sep='\n')
print('*** VENDAS COM MEDIA ACIMA DE R$ 1000 ***')
print(*vendas_maiores, sep='\n')
