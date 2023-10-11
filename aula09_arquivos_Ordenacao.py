import pandas as pd

df_arquivo = pd.read_csv('pokemon.csv')
#print(df_arquivo)
# ORDENE PO NOME
print('****** Ordenação por Nome ******')
print(df_arquivo.sort_values('Name'))
print('****** Ordenação por Speed ******')
print(df_arquivo.sort_values('Speed'))
print('****** Ordenação por Nome e Speed ******')
#  A PRIMEIRA ORDEM SERÁ O NOME
print(df_arquivo.sort_values(['Name', 'Type 1']))
"""
# EXIBIR O TOTAL DE FORMA CRESCENTE
print('********** CRESCENTE *************')
print(df_arquuvo.sort_values('TOTAL',ascending=True))

print('********** DECRECENTE *************')
print(df_arquuvo.sort_values('TOTAL',ascending=False))
"""