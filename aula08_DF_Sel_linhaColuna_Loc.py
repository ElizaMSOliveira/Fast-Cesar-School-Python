import pandas as pd

estados = [ ['Alagoas', 'AL', '3,4 milhoes','Maceió'],
            ['Pernanbuco', 'PE', '9,7 milhoes', 'Recife'],
            ['Ceará', 'CE', '9,2 milhoes', 'Fortaleza'],
            ['Paraíba', 'PB', '1,4 milhoes','Joãp Pessoa',],
            ['Bahia', 'BA', '3,9 milhões', 'Salvador'],
            ['Rio Grande do Norte', 'RN', '1,9 milões', 'Natal']
           ]

df_estados = pd.DataFrame(estados, columns=['ESTADO', 'SIGLA', 'HABITANTES', 'CIDADE'])
ddd = [85, 81, 85, 83,71, 82]

df_estados['DDD'] = ddd
#print(df_estados)
"""O método LOC é usado para selecionar dados com base em rótulos 
de linha e coluna"""
#USANDO O LOC
print(df_estados.loc[0,'CIDADE':'DDD'])
print('****** Pegando Duas Limha ******')
print(df_estados.loc[0:2, 'ESTADO': 'SIGLA'])
print('****** Pegando Fatiada(INDEXAÇÃO) Limha ******')
print(df_estados.loc[2:4,'SIGLA':'CIDADE'])#PEGANDO DA POSIÇÃO 2 INLCUINDO A 4(2,3,4)
