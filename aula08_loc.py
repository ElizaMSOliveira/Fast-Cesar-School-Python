import pandas as pd

estados_nordeste = [['Alagoas', 'AL', '3,4 milhoes','Maceió'],
                    ['Pernanbuco', 'PE', '9,7 milhoes', 'Recife'],
                    ['Ceará', 'CE', '9,2 milhoes', 'Fortaleza']]

#DANDO NOME AS COLUNAS
df_estados_nordeste = pd.DataFrame(estados_nordeste, columns=['ESTADO', 'SIGLA', 'POPULAÇÃO', 'CAPITAL'])

#USANDO O LOC
print(df_estados_nordeste.loc[1:2],'\n')#2° ate a 3°LINHA 
print(df_estados_nordeste.loc[0:1])#1° ate a 2° linha
print('*********Dando nomes **********')
#                            DE:ATE | ESCOLHENDO AS COLUNAS
print(df_estados_nordeste.loc[0:1,['ESTADO', 'CAPITAL']])