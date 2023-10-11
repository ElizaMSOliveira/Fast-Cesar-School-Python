idade = int(input('Qual a idade do atleta? '))


if 16 <= idade <= 18: # idade >= 16 and idade <=18
    print('Juvenil')
elif  14 <= idade <=15:
    print('Infantil')
elif  12 <= idade <= 13:
    print('Mirim')
elif  10 <= idade <= 11:
    print('Pré-Mirim')
else:
    print('Categoria Não Registrada')
