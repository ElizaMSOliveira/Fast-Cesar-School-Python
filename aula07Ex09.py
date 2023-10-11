"""
Crie um programa que utilize o NumPy para calcular 
o retorno total do mês de investimento e o retorno médio semanal
"""
import numpy as np

retorno = np.array([200,300,400,600,150,350,450,120,258,340,
                   200,300,400,600,150,350,450,120,258,340,
                   200,300,400,600,150,350,450,120,258,340])

retorno_mensal = retorno.sum()
print('Retorno de Investimento Mensal R$', retorno_mensal)

media_semanal = retorno_mensal / 4
#media_semanal = retorno.mean()
print('Retorno Médio Semanal R$', media_semanal)