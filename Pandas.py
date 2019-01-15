import pandas as pd
import numpy as np

np.random.seed(101)
df = pd.DataFrame(np.random.randn(5,4), index= 'A B C D E'.split(),columns = ' W X Y Z'.split())
print(df)

print("\nImprimindo a coluna W\n")
print(df['W'])

print("Imprimindo mais de uma coluna:\n")
print(df[['W','X']]) #preciso passar uma lista de lista para imprimir mais de uma coluna

print("Criando uma nova coluna\n")
df['new'] = df['W'] + df['X'] #crio essa coluna chamada new
print(df)

print("\nDeletando uma coluna")
df.drop('new',axis=1,inplace=True) #se o meu axis = 0, estou deletando uma linha (row), se meu axis for = 0, estou deletendo minha coluna, alem disso, se meu inplace estiver = True, estou alterando diretamente meu df
print(df)

print("\nEncontrando um elemento especifico")
print(df.loc['A','W'])

print("\nEcontrando determinados elementos")
print(df.loc[['A','B'],['X','Y','Z']])

print("\nEncontrando elementos usando notacao numpy")
print(df.iloc[1:4,2:]) #pego minha linha de 1 a 4, e a partir da minha segunda coluna

print("\nSeparando elementos que sao maiores que um determinado valor")
print(df[df['W'] > 0]) #noto que, nesse caso, por ter dito para pegar os valores maiores que 0, na coluna W, o meu elemento que está na linha C, será excluído (bem como a linha inteira), pois é menor que 0

print("\nSeprando elementos que sao maiores que um determinado valor e fazendo slice")
print(df[df['W'] > 0]['Y']) #Ou seja, meu DataFrame, mostro meus elementos maiores que 0 na coluna Y, sendo essa relacionada a coluna W, nos quais esses elementos sao maiores que 0
#se o elemente na coluna W é maior que 0, mostro a o elemento equivalente na coluna Y (ou seja, o elemento que está na mesma linha)

print("\nForma equivalente de fazer a mesma função feita acima")
bol = df['W'] > 0
df2 = df[bol] #meu df2 recebe os elementos do df, que na coluna W, sao maiores que 0
print(df2['Y'])

print("\nDefinindo várias condições para mostrar os elementos na minha matriz")
print(df[(df['W'] > 0) & (df['Y'] > 1)])

print("\nResatando o Index da minha matriz")
df.reset_index(inplace=True)
print(df)

print("\nDefinindo novas coluna")
col = 'RS RJ PR SP SC'.split()
df['Estado'] = col
print(df)

print("\nDefinindo novo index")
df.set_index('Estado',inplace=True)
print(df)
