import pandas as pd

df_arquuvo = pd.read_csv('pokemon.csv')
#print(df_arquuvo)
df_arquuvo['TOTAL'] = df_arquuvo['Speed'] + df_arquuvo['Generation']
print(df_arquuvo)# IMPRESSÃO DE TUDO

print(df_arquuvo['TOTAL'])# IMPRESSÃO SO DA COLUNA
df_arquuvo = df_arquuvo[['Name', 'TOTAL']]# CRIANDO 2 COLUNAS [[  ]]
print(df_arquuvo)

# EXIBIR O TOTAL DE FORMA CRESCENTE
print('********** CRESCENTE *************')
print(df_arquuvo.sort_values('TOTAL',ascending=True))

print('********** DECRECENTE *************')
print(df_arquuvo.sort_values('TOTAL',ascending=False))
"""No DataFrame df_pokemon, selecione todos os
nomes Pokémon que têm um Ataque (Attack) maior
que 100 e uma Defesa (Defense) maior que 80."""

print('        EXERCICIO         ')
#attack_maior_100 = df_arquuvo[df_arquuvo['Attack'] > 80]
#df_arquuvo = df_arquuvo[['Name','Attack Maior']]
print(df_arquuvo.columns)
#print(df_arquivo.columns)