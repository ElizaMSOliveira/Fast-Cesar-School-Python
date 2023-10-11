"""Desenvolva um programa que receba o nome de um ciclista,
 a distância que ele percorreu em Km e o tempo que ele gastou
 nesse percurso, em horas.  O programa deverá calcular a velocidade
 média do ciclista e, exibi-la na tela duas vezes, uma em Km/h e
 a outra em m/s. Dividimos por 3,6 quando queremos converter Km/h
 para m/s.
"""
nome = input('Qual o nome do Ciclista? ')
dis = float(input('Qual a distancia Percorrida em Km? '))
tempo = float(input('Qual o Tempo Gasto no percusrso? '))

vm = dis / tempo
ms = vm / 3.6

print('Velocidade Média {} km/h\nVelocidade Média em M/S {:.2f} m/s'.format(vm, ms))