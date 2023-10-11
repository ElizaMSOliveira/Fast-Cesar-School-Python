


qnt_dia = int(input('Qunatos Cigarros em Média você fuma por dia? '))
anos = float(input('Você fuma a quantos anos? '))

dias = anos * 365.25
cigarros = qnt_dia * dias
minutos = (cigarros * 10)
dias_de_vida = minutos / 1440

print('Você fumou {} Cigarros durante {} anos, que são {} Dias'.format(cigarros, anos, dias))
print('Você Perdeu {:.1f} Dias de Sua Vida.\nPare de Fumar Agora!'.format(dias_de_vida))

