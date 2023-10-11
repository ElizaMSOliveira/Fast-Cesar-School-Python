
from random import  randint

soma = 0

def sorteia():
    numeros = []
    for i in range(5):
        numeros.append(randint(0, 99))
    return numeros


def soma_par(numeros):
    pares=[]
    for itens in numeros:
        if itens%2 == 0:
            pares.append(itens)
    print('Valores da lista : {}'.format(numeros))
    print('Valores Pares da lista é {}'.format(pares))
    print('A soma sos valores é {}'.format(sum(pares)))


#print(sorteia())
soma_par(sorteia())