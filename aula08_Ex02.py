import pandas as pd

produtos = {
            'PRODUTO':['Smartphone', 'Laptop', 'Tablet', 'Fone de Ouvido', 'Smart TV'],
            'QNT VENDIDAS':[100, 50, 80, 120,30],
            'PREÇO UNITÁRIO':[800, 2500, 600, 80, 1800]
            }

df_produtos = pd.DataFrame(produtos)
print(df_produtos)
print('********** Adiconando Coluna RECEITA **************')
# receita recebe da df_produtos a coluna QND VENDIDA * da df_produtos a coluna PREÇO UNITÁRIO
receita = df_produtos['QNT VENDIDAS'] * df_produtos['PREÇO UNITÁRIO']
df_produtos['RECEITA'] = receita
print(df_produtos)
print(type(receita))

#Me retornará um boleano ta coluna
print('*************** Retorna os Valores Boleanos Dentro dessa Coluna ***************')
vendas_superior_boo = df_produtos['QNT VENDIDAS'] > 80
print(vendas_superior_boo)
#Me retornará o valor dentro dessa coluna
print('*************** Retorna o Valor dentro dessa Coluna de Acordo com o é Condicionado ***************')
vendas_superior = df_produtos[df_produtos['QNT VENDIDAS'] > 80]
print(vendas_superior)

#print(type(vendas_superior))
#print(type(df_produtos))