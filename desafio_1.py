"""
Desenvolva um programa em Python que apure o resultado de uma votação para determinar o personagem favorito do desenho 
“The Simpsons”. Suponha que existam 2 candidatos cujos códigos são:
1 - Bart
2 - Homer 

Considere que existe uma função que recebe (e escreve em um arquivo .txt ou em) uma lista/vetor os votos de 5 pessoas.
 Um voto é representado pelo código de identificação do candidato.

Na sequência, uma função para leitura deverá ser implementada, a qual deverá apresentar, como resultado:

o nome e a quantidade de votos do candidato mais votado
o nome e a quantidade de votos do menos votado
quantidade de votos nulos (um voto nulo é um voto cujo código de identificação é um valor diferente de 1 e 2). 
"""

bart =[]
homer = []
nulos = []

def votacao(voto):    
    print('Chamou votação')
    if voto == 1:
        bart.append(voto)
    elif voto == 2:
        homer.append(voto)
    else:
        nulos.append(voto)

def ler_voto():
    if len(bart) > len(homer):
        print(f'O candidato 1- Bart foi o condidato mais votado com {len(bart)} votos')

    elif len(homer) > len(bart):
        print(f'O candidato 2- Homer foi o condidato mais votado com {len(homer)} votos')

    elif len(bart) == len(homer) & len(bart) == len(homer)!= 0:
        print(f'Empate Técnico Entro Os Candidato 1- Bart com {len(bart)} votos e 2-Homer com {len(bart)} votos')
    else:
        print('Os Canditados Não Obtiveram Votos')
        
    if len(nulos) != 0:
       print(f'Obtivemos {len(nulos)} votos Nulos')

    else:
        print('Não Obtivemos Votos Nulos')   


cont = 0
while cont <5:
    voto = int(input('|  ELEIÇÃO  |\n|  1 - Bart |\n|  2 Hormer |\n| Digite seu voto: '))
    votacao(voto)
    cont+=1

ler_voto()







