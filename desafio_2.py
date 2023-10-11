"""
Para fazer o desafio, use o seguinte csv:
http://dados.recife.pe.gov.br/dataset/perfil-das-pessoas-vacinadas-covid-19/resource/9664de94-9f07-4adc-848d-b6ef56510762 

Usando a biblioteca pandas, faça alguns filtros  no dataset do link anterior

Selecione as pessoas vacinadas de Recife do sexo feminino da cor parda e preta maior de 60 anos
Selecione as pessoas  que se vacinaram nos meses de abril e maio do sexo masculino
Além do código, escreva no reade.me como você chegou na solução.
"""

import pandas as pd
import datetime as dt

df_vacinados = pd.read_csv('vacinados_CERTO CERTO.csv', nrows=2000)
#CLEARprint(df_vacinados.columns)

print("############ RECIFE- FEMININO - PARDA E PRETA - MAIOR DE 60 ############")
selecionado = df_vacinados[(df_vacinados['municipio'] == 'RECIFE') & (df_vacinados['sexo']== 'FEMININO') & ((df_vacinados['raca_cor'] == 'PARDA') | (df_vacinados['raca_cor'] == 'PRETA')) & (df_vacinados['idade'] > 60) ]
print(selecionado.loc[:, ['municipio','sexo','raca_cor','idade']])

print("######### NOVEMBRO E DEZEMBRO - MASCULINO ###########")
data = df_vacinados[(df_vacinados['sexo']=='MASCULINO') & ((df_vacinados['data_vacinacao'] == '2021-11-30T00:00:00') |(df_vacinados['data_vacinacao'] == '2021-12-30T00:00:00'))]
print(data.loc[:,['data_vacinacao','sexo','municipio']])# print(data.loc[:,'sexo':'municipio']) SE FOSSE DICIONARIO
