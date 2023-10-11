import numpy as np

#CRIANDO ARRAY UNIDIMENSIONAL
array1 = np.array([1, 2, 3, 4, 5])
print(f'Array Unidimensional: {array1}')
print(f'Array Unidimensional Fatiado: {array1[1:4]}')

#ARRAY BIDIMENSIONAL
array2 = np.array([[1, 2, 3], [4, 5, 6]])
print(f'Array Bidimensional: {array2}')
print(f'Array Bidimensional Fatiado: {array2[1:2]}')

#ARRAY TRIDIMENSIONAL
array3 = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
print(f'Arrai Tridimensional: {array3}')

array_zeros = np.zeros((6,6))#1° array 2° elementos do array
print(f'Arrai com Zeros: {array_zeros}')
print(f'Arrai com Zeros Fatiado: {array_zeros[2:6]}')#Do 2° ate o 5° array

#ARRAY COM VALORES ALEATORIOS
array_aleatorios = np.random.rand(2,3)#Serão 2 arrays cada um com 3 elementos aleatorios
print(f'Array com Valores Aleatórios: {array_aleatorios}')
print(f'Array com Valores Aleatórios Fatiado: {array_aleatorios[1:2]}')