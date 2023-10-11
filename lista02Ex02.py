
nome = input('Qual o seu nome? ')
n1 = float(input('Qual a 1° Nota? '))
n2 = float(input('Qual a 2° Nota? '))
n3 = float(input('Qual a 3° Nota? '))

mp = ((n1 * 2) + (n2 * 3) + (n3 * 5)) / 10

#print('A Media final é {:.1f}'.format(mp))

if mp <= 4.9:
    print('Reprovado')
elif mp <= 6.9:
    print('Recuperação')
else:
    print('Aprovado')