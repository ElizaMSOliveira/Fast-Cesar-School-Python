import pandas as pd
#CRIANDO O DICIONARIO
data = {
    'Nome':['Alice', 'Bob', 'Charlie', 'David'],
    'Idade':[25,30,35,40],
    'Cidade':['Nova York','Los Angeles','Chicago','Houston'],
    'TELEFONE':['(01)9929-3339','(02)92353-5698','(03)85235*5475','--']
     }
#CRIANDO O DATAFRAME
df_data = pd.DataFrame(data)

print(df_data)