import pandas as pd

df_arquivo = pd.read_csv('pokemon.csv')
print(df_arquivo.head(20))

"""No DataFrame df_pokemon, selecione todos os
nomes Pokémon que têm um Ataque (Attack) maior
que 100 e uma Defesa (Defense) maior que 80."""

print('        EXERCICIO         ')
# CRIEI UM NODO DATAFRIME QUE RECEBE ESSES VALORES
attack_maior_100 = df_arquivo.loc[(df_arquivo['Attack'] >100) & (df_arquivo['Defense'] > 80)]
df_pokemon1      = df_arquivo.loc[df_arquivo['Attack'] >100 & (df_arquivo['Defense'] > 80)]
# E DELE PEDIR OS NOMES DESSA LISTA
print(attack_maior_100['Name'])
print("*****************************")
#print(df_arquivo.loc[df_arquivo['Attack'] >100 & (df_arquivo['Defense'] > 80)])
print(df_arquivo)
print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
print(attack_maior_100)
"""#df_arquuvo = df_arquuvo[['Name','Attack Maior']]
#print(df_arquivo.loc[df_arquivo['Type 1']== 'Rock'])
print(df_arquuvo.loc[df_arquuvo['Name'],df_arquuvo['Attack'] > 100])
"""