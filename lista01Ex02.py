"""Escreva um programa que leia três valores com ponto flutuante: A, B e
C. Em seguida, calcule e mostre:
a área do triângulo retângulo que tem o valor de A como base e o valor
de C como altura.
a área do círculo que tem como raio o valor de C.
a área do trapézio que tem A e B por bases e C por altura.
a área do quadrado que tem como lado o valor de B.
a área do retângulo que tem lados A e B.
"""
PI = 3.14159
a = float(input('Digite o Valor de A '))
b = float(input('Digite o Valor de B '))
c = float(input('Digite o Valor de C '))

ret = (a*c)/2 #base x altura / 2
cir = PI * (c ** 2) #pi x reaio²
trap = ((a+b)*c)/2 #soma as duas base x altura /2
quad = b ** 2 #base²
retan = a * b #bae x altura

print('TRIANGULO: {:.2f} '.format(ret))
print('CIRCULO: {:.2f} '.format(cir))
print('TRAPÉZIO: {:.2f}'.format(trap))
print('QUADRADO: {:.2f}'.format(quad))
print('RETÂNGULO: {:.2f}'.format(retan))


