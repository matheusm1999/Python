import numpy as np
import pandas as pd

d = {'A':[1,2,np.nan], 'B':[5,np.nan,np.nan],'C':[1,2,3]}
df = pd.DataFrame(d)
print(df)
print("\n")

#posso excluir esses "nan", usando a função df.dropna()
print(df.dropna()) #entretanto, dessa forma, excluo todos os meus índices que possuem algum NaN

print("\nExcluíndo elementos, nas quais as linhas possuem uma quantidade x de valores faltando")
print(df.dropna(thresh = 2))

print("\nPreenche os valores que estão falando com o que eu decidir")
print(df['A'].fillna(value = 'aehoo'))

print("\nSubstituindo valores NaN pela média")
print(df['A'].fillna(value = df['A'].mean()))
