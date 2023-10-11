vel = float(input('Qual a velocidade do carro? '))

valor = (vel - 80) * 5

if vel > 80:
    print('Vc foi Multado e Pagará R$ {}'.format(valor))