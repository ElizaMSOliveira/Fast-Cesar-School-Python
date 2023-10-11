cardapio = {'{coxinha}':5.00, '{pastel}':4.00, '{suco}':3.50, '{bolo}':4.50}


decisao = input('VC quer mudar o Cardapio? S ou N').upper()# passando tudo para maisculo

while  decisao == 'S':
    pergunta = input('Voce Deseja [A]Adicionar. [R]Remover [M]Modificar').upper()

    if pergunta == 'A':
        nome = input('Qual produto Deseja Adicionar?')
        valor = float(input('Qual o Valor desse Produto?'))
        cardapio[nome] = valor # q lista vai receber essa chave[nome] e adicionar o valor a ele

    elif decisao == 'R':
        nome = input('Qual produto deseja remover? ')# Chave para remoçao
        cardapio.pop(nome, 'não encontrado')# ??????

    elif decisao == 'M':
        nome = input('Qual o nome do produto que deseja alterar')# recebe essa chave
        valor = float(input('Qual sera o novo  valor do produto {}? '.format(nome)))
        if cardapio.get(nome):
            cardapio[nome] = valor
            #cardapio.update(nome, valor)
        else:
            print('Nome invalido')
    else:
      print('A Opçao Escolhida é Invalida')

    decisao = input('\n Você deseja fazer mais alguma modificação? ').upper()

print('\n***************** C A R D Á P I O *****************')
print(cardapio)


         
