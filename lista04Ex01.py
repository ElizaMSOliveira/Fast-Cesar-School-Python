
a = []
b = []


for i in range(5):
    a.append(int(input('Digite Valores do Vetor A')))
    b.append(int(input('Digite os Valores do Vetor B: ')))

uniao = a + b # Quando adicionamos vatores em uma variavel, Pytho automaticamente entende que
              # essa Variavel ja passaa ser um vetor(lista)
pares = 0
soma_par = 0
impares = 0
media_impar = 0
for final in uniao:
    if final%2 == 0:
        pares += 1
        soma_par += final
    else:
        media_impar += final
        impares += 1
media = media_impar / impares
print('Soma Pares é {}'.format(soma_par))
print('Media dos Impares é {:.2f}'.format(media))
print('Menor Valor de C é {}'.format(max(uniao)))
