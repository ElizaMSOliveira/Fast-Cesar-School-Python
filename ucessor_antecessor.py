""" Faça um programa que leia um numero imteiro e mostre na tela o
seu Sucessor e seu antecesor"""

n = int(input('Digite um Número: '))
suc = n + 1
ant = n - 1

print('O Sucessor de {} é {} e o seu antecessor é {}'.format(n, suc, ant))