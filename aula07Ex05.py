"""Crie um programa que utilize o Broadcasting do NumPy para converter as 
temperaturas registradas em graus Celsius  para Fahrenheit e Kelvin."""

import numpy as np

temperaturas = np.array([32,18,25,28,40,21,16,33]) 

f_kelvin = 273.15
f_fahrenheit = temperaturas * (9/5) * 32

temperatura_kelvin = temperaturas + f_kelvin
print(temperatura_kelvin)

temperatura_fahrenheit = (temperaturas * (9/5) + 32)
print(temperatura_fahrenheit)