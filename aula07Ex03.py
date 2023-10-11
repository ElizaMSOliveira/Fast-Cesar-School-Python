import numpy as np

notas = ([[6,6,6,10],
          [3,7,7,7],
          [8,8,8,6],
          [9,0,0,0],
          [10,10,10,10]])#posso fazer direto usando np.array

np_notas = np.array(notas)

medias = []
media_maior_7 = []

for notas_de_alunos in np_notas[0:3]:
    medias.append(notas_de_alunos.mean())

for i, maior in enumerate(medias):      
    if maior >= 7:
       media_maior_7.append(f'O Aluno Na {i+1}° Posição Obteve a Nota {maior}')
       

#print(np_notas,'\n')
#print(notas,'\n')
print(medias,'\n')
print(*media_maior_7, sep='\n')
