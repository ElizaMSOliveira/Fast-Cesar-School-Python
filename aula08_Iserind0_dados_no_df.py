import pandas as pd

dados_dos_alunos = []

n = int(input('Quantos Alunos deseja Inserir? '))

for i in range(n):
    nome = input('Qual o nome do Aluno?')
    disciplina = input('Qual a disciplina? ')
    nota = float(input('Qual a nota? '))

    dados_dos_alunos.append({'NOME':nome, 'DISCIPLINA':disciplina, 'NOTA':nota})

print(dados_dos_alunos)

#PASANDO O ARRAY PAR DATAFRAME
df_dados_do_aluno = pd.DataFrame(dados_dos_alunos)
#ADICINANDO COLUNAS
df_dados_do_aluno.columns=['NOME', 'DISCIPLINA', 'NOTA']
print('***********************')
print(df_dados_do_aluno)

