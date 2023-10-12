"""
Leia 4 valores reais que correspondem a 4 notas de um estudante. 
A seguir, calcule a média do estudante.
"""
nota_1 = float(input('Digite a 1° Nota: '))
nota_2 = float(input('Digite a 2° Nota: '))
nota_3 = float(input('Digite a 3° Nota: '))
nota_4 = float(input('Digite a 4° Nota: '))

media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

print(f'MÉDIA = {media}')