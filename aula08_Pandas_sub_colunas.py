import pandas as pd

data = {'A': [10, 20, 30, 40],
        'B': [5, 15, 25, 35],
        'C': [2, 4, 6, 8]}

df_data = pd.DataFrame(data)

df_data['A - C'] = df_data['A'] - df_data['C']
df_data['B x A'] = df_data['B'] * df_data['A']
df_data['C + B'] = df_data['C'] + df_data['B']
df_data['B / C'] = df_data["B"] / df_data['C']
#df_data['MEDIA'] = df_data.mean(df_data = ['C', 'A'])
df_data['MEDIA A'] = df_data['A'].mean()
df_data['MEDIA B'] = df_data['B'].mean()
df_data['MEDIA C'] = df_data['C'].mean()
print(df_data)
