"""
Você é um analista de dados e possui uma matriz com os resultados de testes
realizados por diferentes usuários em um sistema. Crie um programa que utilize 
o fatiamento do NumPy para contar quantos usuários obtiveram resultados
positivos em cada teste
"""
import numpy as np

testes = {
        'Teste_1': ['Positivo', 'Negativo', 'Negativo', 'Positivo','Positivo', 'Negativo', 'Negativo', 'Positivo'],
        'Teste_2': ['Positivo', 'Negativo', 'Negativo', 'Negativo','Negativo', 'Negativo', 'Negativo', 'Positivo'],
        'Teste_3': ['Positivo', 'Positivo', 'Positivo', 'Positivo','Positivo', 'Positivo', 'Positivo', 'Positivo']

}

t1_pos = 0
t2_pos = 0
t3_pos = 0

for pos in testes['Teste_1']:
    if pos == 'Positivo':
      t1_pos += 1
for pos in testes['Teste_2']:
    if pos == 'Positivo':
      t2_pos += 1
for pos in testes['Teste_3']:
    if pos == 'Positivo':
      t3_pos += 1


print(f'{t1_pos} Usuários Tiveram Resultado Positivo no Teste 1')
print(f'{t2_pos} Usuários Tiveram Resultado Positivo no Teste 2')
print(f'{t3_pos} Usuários Tiveram Resultado Positivo no Teste 3')