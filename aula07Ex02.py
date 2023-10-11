import numpy as np

temeratura = np.array([15, 25, 18, 43, 23, 17, 30])

temp_media = np.mean(temeratura)
temp_maxima = np.max(temeratura)
temp_minima = np.min(temeratura)

print(f'A temperatura Média dos Ultimos 7 dias Foi: {temp_media:.2f}')
print(f'A temperatura Máxima dos Ultimos 7 dias Foi: {temp_maxima}')
print(f'A temperatura Mínima dos Ultimos 7 dias Foi: {temp_minima}')