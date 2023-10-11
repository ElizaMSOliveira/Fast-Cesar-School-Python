
total = 0.0

while  True:
    valor = float(input('Digite o valor do produto: '))

    if valor == 0:
        print('Finalizando Programa')
        break
    elif valor < 0 :
        print('Valor inválido')

    total += valor
        #total = total + total

if total > 1000:
    total *= 0.9 # total = total * 0.9
    #total = total - (total * 0.10)
    #total -= total * 0.10 isso é total = - total * 0.10

    print('Total a Pagar R$ {:.2f}'.format(total))