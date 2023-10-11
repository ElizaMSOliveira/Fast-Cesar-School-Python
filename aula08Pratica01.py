import pandas as pd
#Criando o DataFrame a partir de um dicionario
estados_nordeste = [['Alagoas', 'AL', '3,4 milhoes','Maceió'],
                    ['Pernanbuco', 'PE', '9,7 milhoes', 'Recife'],
                    ['Ceará', 'CE', '9,2 milhoes', 'Fortaleza']]
#Se fosse lista
"""
estados_nordeste2 = {'Estado': 'Alagoas', 'AL', '3,4 milhoes','Maceió',
                    ['Cidade': 
                     'UF':
                      'Habitantes': ernanbuco', 'PE', '9,7 milhoes', 'Recife'],
                    ['Ceará', 'CE', '9,2 milhoes', 'Fortaleza']}
"""
df = pd.DataFrame(estados_nordeste)
#CRIANDO E NOMEANDO AS COLUNAS
df_criando_colunas = pd.DataFrame(estados_nordeste, columns=['ESTADO', 'SIGLA', 'HABITANTES',  'CIDADE'])

#print(df)
print(df_criando_colunas, '\n')
#ADICIONANDO OS DADOS A UMA VARIAVEL
idh = [0.659, 0.5897, 0.4872]
#ADICINANDO UMA COLUNA E COLOCANDO A VARIAVEL CRIADA ANTES
                #dando nome a ela
df_criando_colunas['IDH'] = idh
print(df_criando_colunas,'\n')
print(df_criando_colunas['ESTADO'],'\n')#exibir apenas o elemento estado
print(df_criando_colunas[['ESTADO', 'HABITANTES', 'SIGLA']])#exibir dois elemento


