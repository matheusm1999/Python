#Usando o modelo de Regressão linear para estimar o preço de casas, com base em suas características
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#%matplotlib inline

USAhousing = pd.read_csv('C:/Users/mathe/OneDrive/Documentos/LABI/Python/Python-Data-Science-and-Machine-Learning-Bootcamp/5.MachineLearning/RegressoesLineares/USA_Housing.csv')
print(USAhousing.head())
print(USAhousing.info())

sns.pairplot(USAhousing) #Percebo que há uma relação linear quanto ao preço
sns.heatmap(USAhousing.corr())

#Separando minhas features da minha classe
X = USAhousing[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms','Avg. Area Number of Bedrooms', 'Area Population']] #Pego todas minhas columas menos a columa preço e endereço (pois é nominal)
Y = USAhousing['Price'] #A coluna preço é a minha variável dependente

#Separando os dados de treino e de test
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.4,random_state = 101)
print(X_test.shape[0]) #Ou seja, 2000 dados para treino

#Usando o algoritmo linear Regression
from sklearn.linear_model import LinearRegression
modelo = LinearRegression()
modelo.fit(X_train,Y_train)

coefs = pd.DataFrame(modelo.coef_,X.columns,columns = ['coefs'])
print(coefs) #Percebo que, por exemplo, se aumentar em uma unidade (um ano) a idade média das casas, haverá o aumento de U$164883.282027 

resultado = modelo.predict(X_test)

#Plotando o resultado
plt.figure(figsize=(12,6))
plt.scatter(Y_test,resultado) #No eixo x, tenho o valor correto, e no eixo y, tenho o valor que o modelo predisse. Observo que o modelo teve um bom desempenho. Se fosse perfeito, teria uma linha reta.

sns.distplot((Y_test-resultado)) #Vejo que se aproxima de uma distribuição normal, portanto o desempenho do modelo foi bom
