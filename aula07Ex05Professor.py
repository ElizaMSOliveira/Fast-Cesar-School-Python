""" Exercício 5 Crie um programa que utilize o Broadcasting do NumPy para converter as temperaturas
 registradas em graus Celsius para Fahrenheit e Kelvin.
"""
import numpy as np

temperaturas_celsius = np.array([32, 31.5, 27.8, 29, 32.5, 33, 31, 24, 22.5, 26, 28.5])

aditivo_kelvin = 273.15 # c + 273.15
fator_fahrenheit = 0 # (c * 9/5) + 32
""" Podemos simplesmente fazer uma adição simples, que a propriedade de Broadcasting
dos arrays criados pelo numpy se encarregam de fazer a operação em todos os itens """

temperaturas_kelvin = temperaturas_celsius + aditivo_kelvin
print(temperaturas_kelvin)
""" Mesma coisa aqui, plugamos o array na equação que converte pra Fahrenheit
e o numpy se encarrega de realizar a operação para cada item """

temperaturas_fahrenheit = (temperaturas_celsius * (9/5)) + 32
print(temperaturas_fahrenheit)