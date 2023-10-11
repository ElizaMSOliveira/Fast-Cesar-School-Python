
notas = []

for i in range(5):
    nota = float(input('Difite a Nota'))
    notas.append(nota)
#print(notas)
media = sum(notas)/len(notas)
print('A Média é: {}'.format(media))

for i in range(len(notas)):
    if notas[i] > media:
        print('A nota {} é mior que a média {}'.format(notas[i], media))