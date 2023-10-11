import pandas as pd

estados = [['Alagoas', 'AL', '3,4 milhoes','Maceió'],
                    ['Pernanbuco', 'PE', '9,7 milhoes', 'Recife'],
                    ['Ceará', 'CE', '9,2 milhoes', 'Fortaleza'],
                    ['Paraíba', 'PB', '1,4 milhoes','Joãp Pessoa',],
                    ['Bahia', 'BA', '3,9 milhões', 'Salvador'],
                    ['Rio Grande do Norte', 'RN', '1,9 milões', 'Natal']
                    ]
#                                   INERINDO NOMES AS COLUNAS
pd_estados = pd.DataFrame(estados, columns=['ESTADO', 'SIGLA', 'HABITANTES', 'CIDADE'])
#print(estados)
print(pd_estados)

# CCRIANDO AS COLUNAS
ddd = [85, 81, 85, 83,71, 82]
# INSERINDO COLUNAS
pd_estados ['DDD'] = ddd
print(pd_estados)


