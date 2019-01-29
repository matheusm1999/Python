#Projeto que prediz se o usuário clicará ou não em uma propaganda utilizando Regressão Logística
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

ad_data = pd.read_csv("C:/Users/mathe/OneDrive/Documentos/LABI/Python/Python-Data-Science-and-Machine-Learning-Bootcamp/5.MachineLearning/RegressaoLogistica/advertising.csv")

ad_data.head()# Verifico as informações contidas no Data Frame

ad_data.describe() #Vejo que tenho um total de 1000 entradas

ad_data.info()

#Análise Exploratória de Dados
#Verificando se há dados nulos
ad_data.isnull().values.any() #Vejo que não há

#Plotando as idades em um histograma, para ver a sua distribuição
sns.set_style('whitegrid')
ad_data['Age'].hist(bins=30) #O motivo ter escolhido o histograma, é porque é um gráfico específico para trabalhar com variáveis contínuas
plt.xlabel('Idade')
#Vejo que há bastante pessoas com idades entre 30-40 anos. Sendo a média de idade, 36 anos

#Vendo se a média da renda do consumidor por região possúi alguma relação com a idade
sns.jointplot(x='Age',y='Area Income',data = ad_data)
#Pelo que pode ser observado, a maior parte da renda vem de idades entre 25 e 40 anos
#Ou seja, pessoas mais jovens dão uma renda maior

#Vendo se há alguma relação entre idade e tempo gasto diariamente no site
sns.jointplot(x='Age',y='Daily Time Spent on Site',kind= 'kde', data  = ad_data)
#Posso ver que pessoa entre 20 e 40 anos, gastam mais tempo no site, diáriamente, enquanto pessoas mais velhas gastam menos tempo
#Posso observar também ,que há uma grande concentração de pessoa que possuem aproximadamenter 31 anos, e gastam cerca de 78 minutos diários nesse site

#Verificando agora, a relação entre tempo que o consumidor gasta na internet, e quanto tempo gasta no site
sns.jointplot(x = 'Daily Internet Usage',y = 'Daily Time Spent on Site',data = ad_data,color = 'purple')
#Posso ver que quanto mais tempo a pessoa gasta online, mais tempo essa pessoa gasta no site
#Entretanto, isso não ocorre entre os valores de 100 e 175 minutos gastos diários na internet
#Uma vez que podemos observar, pelo gráfico, que nesse intervalo, quanto mais tempo a pessoa gasta online, menos ela tende a ficar nesse site
#Mas isso muda uma vez que o valor de 200 minutos gastos online aparece
#A partir desse valor, podemos ver que quanto mais tempo gasto online, mais tempo a pessoa gasta nesse site

sns.pairplot(ad_data)

#Separando em dados de treino e de teste
x = ad_data[['Daily Time Spent on Site', 'Age', 'Area Income','Daily Internet Usage', 'Male']]
y = ad_data['Clicked on Ad']

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.33,random_state=42)

#Treinando e aplicando meu modelo
from sklearn.linear_model import LogisticRegression
modelo = LogisticRegression()
modelo.fit(x_train,y_train)
resultado = modelo.predict(x_test)

#Vendo a eficácia do meu modelo
from sklearn.metrics import confusion_matrix,classification_report
matriz = confusion_matrix(y_test,resultado)
avaliacao = classification_report(y_test,resultado) #Aqui, posso ver que a precisão foi de 91%
print(matriz)
print(avaliacao)
print("O modelo acertou {} e errou {}, de um total de 330".format(matriz[0][0] + matriz[1][1], matriz[0][1] + matriz[1][0] ))
print("Portanto, a precisão foi de 91%")
