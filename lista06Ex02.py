"""
Desenvolva uma função que permita receber uma variável inteira X
 inúmeras vezes (deve parar quando o valor digitado for igual a
 zero). Como retorno da função, para cada valor lido deverá ser
 imprimido a sequência de 1 até X (o número digitado),
 com um espaço entre cada número e seu sucessor.
"""

def vezes(num):
    vezes = 1
    while vezes <=num:
        if num != 0:
            print(vezes, end=' ')#Tira a impressao em fila e coloca espaço
            vezes += 1
        else:
         break


vezes(0)