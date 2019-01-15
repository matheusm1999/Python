import pandas as pd
df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
print(df)
print('\n')

#Pegando elementos únicos (não cópias) do meu DataFrame
print(df['col2'].unique())

#mostrando a quantidade de elementos únicos
print('\nTamanho de unicos: {}'.format(df['col2'].nunique() ) )

#Fazendo alguma operação com o meu DataFrame
def vezes2 (x):
    return x*2

print(df['col1'].apply(vezes2)) #essa função é passada para cada elemento do meu df

print('\nPegando o tamanho de String da coluna 3')
print(df['col3'].apply(len))

#Fazendo o quadrado de cada elemento usando uma função lambda
print('\n')
print(df['col1'].apply(lambda x: x*x))

print('\nDeletando alguma coluna')
#del df['col2']
print(df)

print("\nSabendo quais são as colunas existentes")
print(df.columns)

print("\nSabendo quais são os meus índices")
print(df.index) #vai dizer que começa em 0 e termina em 4

print("\nOrdenando uma coluna especifica")
print(df.sort_values(by = 'col2')) #lembrando que o inplace desse método, é False por padrão
