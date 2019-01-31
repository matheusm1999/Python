#Prevendo qual será a iris utilizando Support Vector Machines
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Importando os dados
iris = sns.load_dataset('iris')

#Análise de dados exploratórios
iris.head()

iris.info() #Ao todo tenho 150 dados

sns.pairplot(iris, hue = 'species', palette = 'Dark2') #Vejo que a íris setosa é bem diferenciável das outras duas

#Criando um dataframe apenas com a iris setosa
setosa = iris[iris['species'] == 'setosa']
#Fazendo um plot Comprimento x Largura
sns.kdeplot(setosa['sepal_width'],setosa['sepal_length'],cmap = "plasma",shade = True,shade_lowest=False)

#Dividindo entre dados de treino de teste
from sklearn.model_selection import train_test_split
x = iris.drop('species',axis = 1) #retiro minha coluna "species", criando assim um dataframe com minhas variáveis preditoras
y = iris['species']
x_train,x_test,y_train,y_test = train_test_split(x,y)

#Treinando e aplicando meu modelo
from sklearn.svm import SVC
modelo = SVC() #Usando os parâmetros default
modelo.fit(x_train,y_train)
resultado = modelo.predict(x_test)

#Avaliando meu modelo
from sklearn.metrics import confusion_matrix,classification_report
print(confusion_matrix(y_test,resultado))
print(classification_report(y_test,resultado))
#Vejo que o resultado do meu modelo foi de 100%
