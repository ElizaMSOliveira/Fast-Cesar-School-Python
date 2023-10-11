
""" Exercício 4
Crie um programa que utilize o NumPy para calcular a média de vendas nos primeiros 10 dias e verificar
se houve algum dia em que as vendas foram maiores que 1000. ‍‍
"""
import numpy as np

lista_vendas_mes = np.array([253, 780, 2819, 170, 4753, 3006, 304, 3916, 3315, 1055, 706, 5051, 3583, 962, 408, 815, 819, 3160, 4818, 185, 772, 460, 791, 1186, 896, 883, 1125, 4773, 713, 907])

# Médias dos primeiros 10 dias
medias_primeiros_dez_dias = lista_vendas_mes[0:10].mean()
print(medias_primeiros_dez_dias)

# Quais dias tivemos boas vendas (vendas acima de 1000)
dias_de_boas_vendas = []
for dia in range(0, 30):
    if lista_vendas_mes[dia] >= 1000:
        dias_de_boas_vendas.append(f"Dia {dia+1} foi um bom dia de vendas")
# Aquele mesmo print do exercício 3, com o separador para pular linhas
print(*dias_de_boas_vendas, sep="\n")

# Se tivemos pelo menos um dia com vendas acima de 1000
if lista_vendas_mes.max() >= 1000:
    print("Tivemos um bom dia de vendas")
