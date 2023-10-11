import pandas as pd

estudantes = {
    'NOME':['Eliza', 'Jael', 'Lita', 'Rita', 'Fulana'],
    'IDADE':[44, 17, 22, 25 ,35],
    'MEDIA DE NOTAS':[8.5, 7.8, 9.2, 6.5, 8.9]
    }

pd_estudantes = pd.DataFrame(estudantes)
print(pd_estudantes)
status = ['Aprovado', 'Aprovado', 'Aprovado', 'Reprovado', 'Aprovado']
pd_estudantes['STATUS'] = status
print('****** Adicionei Coluna Status ******')
print(pd_estudantes)

#ERRO DF RECEBE DF ESTUDANTE QUE TEM A COLUNA STATUS == APROVADO
#aprovados = pd_estudantes['STATUS'=='Aprovado'] 
# DF RECEBE A DF pd_estudante PEGANDO DA DF ESTUDANTE A TABELA STATUS IGUAL A REPROVADO
df_reprovado = pd_estudantes[pd_estudantes['STATUS'] == 'Reprovado']

print(df_reprovado)
print('******* Selcionando colunas com LOC ******')
print(df_reprovado.loc[:, 'NOME':'IDADE'])
print('******* Selcionando colunas com ILOC ******')
print(df_reprovado.loc[:, :])

#PG 27