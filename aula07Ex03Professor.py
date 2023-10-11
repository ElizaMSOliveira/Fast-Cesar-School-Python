""" Exercício 3
Crie um programa que utilize o NumPy para realizar análises específicas sobre as notas, como calcular
a média das notas dos três primeiros alunos e verificar quais alunos tiraram notas acima de 7. ‍‍
"""
import numpy as np

# Exemplo de notas em uma matriz

notas_alunos = np.array([[7, 5, 8, 9], # lista nº 0, aluno 1
                         [2, 6, 6, 4], # lista nº 1, aluno 2
                         [9, 9, 9.5, 7], # lista nº 2, aluno 3
                         [8, 10, 10, 6], # lista nº 3, aluno 4
                         [2, 4, 6, 6.5], # lista nº 4, aluno 5
                         ])

# Lista simples para armazenar as médias dos alunos. Também poderia ser um array do numpy
medias = []
# Aqui varremos a lista de notas até o terceiro índice
for notas_de_cada_aluno in notas_alunos[0:3]:
# E com .append() nós anexamos a nota para a lista de médias
    medias.append(notas_de_cada_aluno.mean())

print(medias)
# Agora uma lista para armazenar quais alunos tiraram pelo menos uma nota acima de 7
uma_nota_acima_de_7 = []
# Varremos esta lista utilizando o índice para podermos referenciar o aluno
for aluno in range(len(notas_alunos)):
 # Conferimos se a maior nota do aluno é acima de sete
 if notas_alunos[aluno].max() >= 7:
 # E se sim, acrescentamos esta frase na lista
    uma_nota_acima_de_7.append(f"Aluno {aluno+1} tirou uma nota acima de sete")

print(*uma_nota_acima_de_7, sep="\n")
"""Este print acima é feito de uma forma um pouco diferente, já que desejamos
exibir o conteúdo dessa lista de forma mais distinta. Se utilizássemos ele
normalmente, exibiria o resultado como ["frase 1", "frase 2", "frase 3"], mas
podemos melhorar isso.
Quando passamos o * antes do nome da lista, estamos indicando para o print que
ele deve imprimir cada item da lista de forma separada, como se cada item
fosse uma nova chamada do print().
O parâmetro "sep" que indicamos depois, é como o print deve separar cada um
destes itens. Neste caso, separamos com uma quebra de linha (\n)
Desta forma ele imprimirá:
frase 1
frase 2
frase 3
"""