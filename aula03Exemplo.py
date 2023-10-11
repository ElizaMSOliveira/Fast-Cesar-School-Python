

n = int(input('Digite Um Número INteiro: '))
soma = 0

# i vai representar o divisor do numero
    # começa, termina, passo de
for i in range(1, n, 1):

    if n % i == 0:
        soma += i

# Um Número é perfeito quando a soma dos divisores é igual
# ao prorpio numero
if n == soma:
    print('Numero Perfeito')
else:
    print('Não é um numero perfeito')

