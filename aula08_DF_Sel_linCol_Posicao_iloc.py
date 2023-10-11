import pandas as pd
#DICIONARIO
estados =  {
            'ESTADO':    ['Alagoas','Pernanbuco','Ceará','Paraíba','Bahia','Rio Grande do Norte'],
            'SIGLA':     ['AL','PE','CE', 'PB','BA','RN'],
            'POPULAÇÃO': ['3,4 milhoes','9,7 milhoes','9,2 milhoes','1,4 milhoes','1,9 milões','3,9 milhões'],
            'CIDADE':    ['Maceió','Recife', 'Fortaleza', 'JoãO Pessoa', 'Salvador', 'Natal']
            }

df_estados = pd.DataFrame(estados) #Se quiser podemos atualizar os nomes columns=['eSTADO', 'sIGLA', 'hABITANTES', 'cIDADE'])
ddd = [85, 81, 85, 83,71, 82]

df_estados['DDD'] = ddd
print(df_estados)
print('******** SELECINANDO LINHAS ************')
print(df_estados.iloc[1:3])#Posicão 1 e 2 a 3 não entra
print('******** LINHAS |||| COLUNAS ************')
print(df_estados.iloc[0:2, 2:4])#LINHA 0,1, COLUNA 2,3