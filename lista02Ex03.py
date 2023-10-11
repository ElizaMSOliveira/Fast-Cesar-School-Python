
min = int(input('Faltam Quantos Minutos para ir embora? '))
tempo_fab = int(input('Quanto tempo para Cada Presente? '))

if tempo_fab * 2 <= min:
    print('Da Tempo!')
else:
    print('Deixa para Amanhã')
