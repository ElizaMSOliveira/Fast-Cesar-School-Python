import numpy as np

array = np.array([[1, 2, 3, 4, 5, 6], [21, 31, 41, 51, 61, 71]])
array2 = np.array([7, 8, 9, 10, 11, 12])

#SOMA DE TODOS VALORES DE UM ARRAY
soma = np.sum(array)#SUM É A SOMA DE TODOS OS VALORES
print(f'A soma de Todos Elementos: {soma}')
#O VALOR MAXIMO DE UM ARRAY
maximo = np.max(array)#MAX É O VALOR MAXIMO ENTRE OS VALORES
print(f'O NUmero Maximo do Array: {maximo}')
#O VALOR MINIMO DE UM ARRAY
minimo = np.min(array)#MIN É O MENOR VALOR DE UM ARRAY
print(f'O valor Minimo de Um Array: {minimo}')
#A MEDIA DA SOMA DOS ELEMENTOS
media = np.mean(array)
print(f'TESTE {media}')
#BROADCASTING
juncao = array + array2#Soma os elementos do array Bidimensional ao unidimensional
print(f'Juntando os dois Arrays: {juncao}')
