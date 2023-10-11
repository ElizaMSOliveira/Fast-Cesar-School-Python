import pandas as pd

estados = [ ['Alagoas', 'AL', '3,4 milhoes','Maceió'],
            ['Pernanbuco', 'PE', '9,7 milhoes', 'Recife'],
            ['Ceará', 'CE', '9,2 milhoes', 'Fortaleza'],
            ['Paraíba', 'PB', '1,4 milhoes','Joãp Pessoa',],
            ['Bahia', 'BA', '3,9 milhões', 'Salvador'],
            ['Rio Grande do Norte', 'RN', '1,9 milões', 'Natal']
           ]
#CRIADO O DF E JA DANDO NOMES AS COLUNAS
df_estados = pd.DataFrame(estados, columns=['ESTADO', 'SIGLA', 'HABITANTES', 'CIDADE'])

#INSERINDO COLUNAS
ddd = [85, 81, 85, 83,71, 82]
df_estados['DDD'] = ddd
#IPRESSAO DE TODA A TABELA
print(df_estados)

#IMPRESSÃO DE TABELAS SELECIONADAS
print(df_estados['ESTADO'])# DEVE SER IGUAL AO NOME DA COLUNA

#IMPRESSAO DE MAIS DE UMA COLINA

print(df_estados[['ESTADO', 'DDD']])#SE FOT MIS DE UMA COLUNA DUAS CHAVES SEPARADOS POR , E ENTRE ''

