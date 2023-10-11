import pandas as pd

data = {'A': [10, 20, 30, 40],
        'B': [5, 15, 25, 35],
        'C': [2, 4, 6, 8]}

df_data = pd.DataFrame(data)

df_data['MEDIA A'] = df_data['A'].mean()
df_data['MEDIA B'] = df_data['B'].mean()
df_data['MEDIA C'] = df_data['C'].mean()
#  AXIS=1 ==> LINHA A LINHA EM CADA COLUNA
df_data['MEDIA A e C'] = df_data[['A','C']].mean(axis=1)
df_data['MEDIA B e C'] = df_data[['B', 'C']].mean(axis=1)
df_data['MEDIA A, B e C'] = df_data[['A', 'B', 'C']].mean(axis=1)
print(df_data[['MEDIA A','MEDIA B','MEDIA C','MEDIA A, B e C']])