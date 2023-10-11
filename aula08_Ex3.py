import pandas as pd

alunos = {'NOME':['Eliza', 'José', 'Ana', 'Maria', 'Barbara'],
          'NOTA_1': [8, 7.5, 7, 5, 10],
          'NOTA_2':[6, 8, 8.5, 6.4, 7.6]
          }

df_alunos = pd.DataFrame(alunos)

df_alunos['MEDIA']= df_alunos[['NOTA_1', 'NOTA_2']].mean(axis=1)
print(df_alunos)
