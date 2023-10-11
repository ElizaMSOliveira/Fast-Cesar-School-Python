
respostas = []
print(type(respostas))
sim = 0
respostas.append(input('Conhece a Vitima do Furto? '))
respostas.append(input('Esteve no Locas do Furto? '))
respostas.append(input('Mora Perto da Vitima? '))
respostas.append(input('A Vitima lhe devia? '))
respostas.append(input('Já trabalhou com a Vitima? '))
print(respostas)

for i in range(5):
    if respostas[i] == 'sim':
        sim += 1

if respostas.count('sim') == 2:
 print('Suspeita')
elif respostas.count('sim') >=3 and respostas.count('sim') <= 4:
 print('Cumplice')
elif respostas.count('sim') == 5:
 print('Ladrão')
else:
 print('Inocente')