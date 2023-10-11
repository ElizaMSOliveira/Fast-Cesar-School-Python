import pandas as pd

data = {'A': [10, 20, 30, 40],
        'B': [5, 15, 25, 35],
        'C': [2, 4, 6, 8]}

df_data = pd.DataFrame(data)
#SUM SOMA TODOS VALORES DA COLUNA
df_data['SUM A'] = df_data['A'].sum()
df_data['MEDIA B'] = df_data['B'].sum()
df_data['MEDIA C'] = df_data['C'].sum()
print(df_data)
#Soma todas as colunas de todas somas
print('***********************')
soma = df_data.sum()
print(soma)
print('********Diferença entre Soma e SUm')
df_soma_A = df_data['Soma A + C'] = df_data['A']+ df_data['C']
sum_A = df_data['Sum() A']= df_data['A'].sum()
print('***** Soma de A e C **********')
print(df_soma_A)
print('********* SUM de A **********')
print(sum_A)