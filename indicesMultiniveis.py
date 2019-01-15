import numpy as np
import pandas as pd

outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))#o método zip, associa os valores outside com os valores de inside. Traforma as listas em uma tupla
hier_index = pd.MultiIndex.from_tuples(hier_index) #objeto do pandas que cria multi índices
df = pd.DataFrame(np.random.randn(6,2),index = hier_index, columns = ['A','B'])
print(df) #noto que, meu g1 e g2 servem de índices secundários


print("\nMostrando os elementos do índice secundário G1")
print(df.loc['G1'])

print("\nMostando os elementos do índice secundário G1, com index 1")
print(df.loc['G1'].loc[1])

df.index.names = ['Grupos', 'Numero']
print(df)

print("Mostrando valores de diferentes seções")
print(df.xs(1,level = 'Numero')) #dessa forma, pego meu grupo interno(Numero) e imprimo aqueles que estão no índice 1
