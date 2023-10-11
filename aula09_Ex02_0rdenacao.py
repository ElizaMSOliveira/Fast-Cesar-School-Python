"""
Ordene o DataFrame df_pokemon em ordem
crescente com base no type 1 e nos nomes dos
Pokémons. Exiba os 10 primeiros nomes e tipos
Pokémons."""

import pandas as pd

df_arquivo = pd.read_csv('pokemon.csv')
#print(df_arquivo.head(20))
#ORDEM CRESCENTE POR TYPE 1 E NOS NOMES
print(df_arquivo.sort_values(['Type 1','Name'], ascending=True).head(10))

# PROFESSORA
"""
import pandas as pd
df_pokemon = pd.read_csv('pokemon.csv')
df_pokemon = df_pokemon.sort_values(['Type 1','Name'])
print(df_pokemon.head(10)[['Name','Type 1']])
"""
# FAER EXEMPLO 3