import pandas as pd

estados_nordeste = [['Alagoas', 'AL', '3,4 milhoes','Maceió'],
                    ['Pernanbuco', 'PE', '9,7 milhoes', 'Recife'],
                    ['Ceará', 'CE', '9,2 milhoes', 'Fortaleza'],
                    ['Paraíba', 'PB', '1,4 milhoes','Joãp Pessoa',],
                    ['Bahia', 'BA', '3,9 milhões', 'Salvador'],
                    ['Rio Grande do Norte', 'RN', '1,9 milões', 'Natal']]

#CRIANDO DATAFRAME
df_estados_ne = pd.DataFrame(estados_nordeste)
print(df_estados_ne)
#CRIANDO AS COLUNAS
print(df_estados_ne)
df_estados_ne.columns=['ESTADO', 'SIGLA', 'POPULAÃO', 'CAPITAL']
print(df_estados_ne)
#VERIFICANDO O TIPO
print(type(df_estados_ne))
#CRIANDO DATAFRAME DIRETO COM AS COLUNAS
#df_estados_ne = pd.DataFrame(estados_nordeste, columns=['ESTADO', 'SIGLA', 'POPULAÃO', 'CAPITAL'])
#print(df_estados_ne)

#1:18 adicionar nonas colunas
#slide aula_08 DataFrame pag14