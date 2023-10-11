import pandas as pd

df_pokemon = pd.read_csv('pokemon.csv')
#Exibe os 5 primeiros e 5 ultimos da lista
print(df_pokemon)
print('***** Escolhedo as Limhas para Visualizar *****')
print(df_pokemon.head(10))
print('*****  Visualizar As Ultimas Linhas *****')
print(df_pokemon.tail())
print('***** Escolhedo as Utimas Limhas para Visualizar *****')
print(df_pokemon.tail(2))