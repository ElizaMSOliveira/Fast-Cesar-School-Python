
import numpy as np

#CRIANDO OS ARRAYS

array_1 = np.array([1, 3, 5, 7])
array_2 = np.array([2, 4, 6, 8])
array_3 = np.array([10, 20, 30, 40])

#SOMA DE ARRAY
soma = array_1 + array_3
print(f'Soma de Arrays: {soma}')

#SUBATRAÇÃO DE ARRAY
subtracao = array_3 - array_1
print(f'Subtração de Array: {subtracao}')
print(f'Subtração de Array: {subtracao[1:3]}')#Subtraindo 0 2° e o 3° item

#MULTIPLICAÇÃO DE ARRAY
multiplicacao = array_2 * array_3
print(f'Multiplicação de Arrays: {multiplicacao}')
print(f'Multiplicação de Arrays Fatiado: {multiplicacao[1:3]}')

#DIVISÃO DE ARRAY
divisao = array_1 / array_2
print(f'Divisão de Arrays: {divisao}')
print(f'Divisão de Arrays Usando Raund: {np.round(divisao, 2)}')#Round usa as casas decimais
print(f'Divisão de Arrays Fatiado: {np.round(divisao[2:4], 2)}')#O 1° elemento é o que será impresso e  o 2° a qnt de casas decimais

#EXPONENCIAÇÃO
exponenciacao = np.power(array_3, 2)#Array 3 elevado a potencia.
print(f'Exponencioação de Array: {exponenciacao}')
print(f'Exponencioação de Array: {exponenciacao[0:2]}')#So o 1° e 2° elemento

