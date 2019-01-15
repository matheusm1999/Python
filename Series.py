import numpy as np
import pandas as pd

#criando uma lista e transformando a mesma em um array
labels = ['a','b','c']
minha_lista = [10,20,30]
array = np.array([minha_lista])
print(array)

#criando um dicionário
d = {'a':10,'b':20,'c':30}

#agora, crio uma series, no panda, onde cada elemento/data(minha_lista) estará associado um índice (labels)
#É basicamente, um dicionário
serie = pd.Series(data = minha_lista,index = labels)
print(serie)

#Outro exemplo de série
serie1 = pd.Series([1,2,3,4], index = ['Alemanha','Italia','EUA','Japão'])
print(serie1)

serie2 = pd.Series([1,2,3,4], index = ['Brasil','EUA','Japão','URSS'])
print(serie2)

#Além disso, posso fazer operações matemáticas com essas Séries
print(serie1 + serie2)
#aqui ele soma valor dos eua na serie 1 (3) + valor dos eua na série 2 (2) = 5
#Valores que não estiverem em comum nas duas séries, aparecem como "NaN"
