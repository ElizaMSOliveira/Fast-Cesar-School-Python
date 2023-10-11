"""Desenvolva um programa que leia a largura e altura de uma
 parede, calcule e mostre a área a ser pintada e a quantidade de
 tinta necessária para o serviço, sabendo que cada
litro de tinta pinta uma área de 2 metros quadrados (m²)."""

largura = float(input('Qual a Largura da Parede? '))
altura = float(input('Qual a Altura da Parede? '))
area = largura * altura
tinta = area / 2

print('A Parede tem {}m²\nSerá preciso {} baldes de tinta'.format(area, tinta))
