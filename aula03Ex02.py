nota = 0
cont = 0
media = 0
while True:
    n = float(input('Digite a Nota: '))

    if n < 0:
        print('Finalizando Programa')
        break
    else:
        nota += n
        cont += 1

media = nota/cont

print(cont)
print(media)
