import pandas as pd

df_arquivo = pd.read_csv('pokemon.csv')

print(df_arquivo)
#VISUALIZANO COLUNAS
print('***** Visualizando Colunas *****')
print(df_arquivo.columns)
#VIZUALIZAR INFORMAÇÕES DAS COLUNAS
#COMEÇA TERMINA PASSOS
print('***** Visualizando informações das Colunas *****')
print(df_arquivo.index)
print('***** iNFORMAÇÕES SOBRE DATAFRAME *****')
print(df_arquivo.info)
print('***** Visualizando Por Nomes *****')
print(df_arquivo['Name'])
print('***** Visualizando Por Nomes e Sp.Atk*****')
print(df_arquivo[['Name', 'Sp. Atk']])
