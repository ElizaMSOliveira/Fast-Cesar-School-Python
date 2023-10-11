par = 0
impar = 0
for i in range(10):
    n = int(input('Digite um Numero: '))

    if n % 2 == 0:
        par += 1
    else:
        impar += 1

print('{} Numeros Pares'.format(par))
print('{} Números Impar'.format(impar))

