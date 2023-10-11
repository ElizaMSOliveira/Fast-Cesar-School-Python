import pandas as pd

df_arquivo = pd.read_csv('pokemon.csv')
#print(df_arquivo)
#print('***** Visualizando Por Nomes *****')
#print(df_arquivo['Name'])
#print('***** Visualizando Por Nomes e Sp.Atk*****')
#print(df_arquivo[['Name', 'Sp. Atk']])
#FILTRO DE ARQUIVOS
print('***** Esolha a Coluna e selecione o que Deseja *****')
print(df_arquivo.loc[df_arquivo['Legendary']== True])
print(df_arquivo.loc[df_arquivo['Type 1']== 'Rock'])