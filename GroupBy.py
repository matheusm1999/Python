import pandas as pd
data = {'Empresa': ['GOOG','GOOG','MSFT','MSFT','FB','FB'], 'Nome': ['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],'Venda': [200,120,340,124,243,350]}
df = pd.DataFrame(data)
print(df)

#Fazendo um agrupamento
group = df.groupby('Empresa') #faço um agrupamento por nome
print(group.sum()) #Mostro soma das vendas de cada 'Empresa' diferente

print('\n')
group2 = df.groupby('Nome')
print(group2.sum().loc['Amy']) #mostro o total de vendas da Amy
