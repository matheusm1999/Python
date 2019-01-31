#Prevendo se uma pessoa terá ou não câncer de mama usando o algorítmo Support Vector Machine
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

%matplotlib inline

from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()

cancer.keys() #Verificando os dados

print(cancer['DESCR']) #Ao todo, tenho 569 entradas

#Agora, vou criar um data frame com esses dados
df_cancer = pd.DataFrame(cancer['data'],columns = cancer['feature_names'])

print(df_cancer.head())

df_target = pd.DataFrame(cancer['target'],columns = ['Cancer']) #Criando um data frame com a minha variável dependente
print(df_target)

#Separando em dados de teste e de treino
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(df_cancer,np.ravel(df_target),test_size = 0.3, random_state = 101) #np.ravel para converter em array

#Treinando e aplicando meu modelo
from sklearn.svm import SVC
modelo = SVC(kernel = 'rbf')
modelo.fit(x_train,y_train)
resultado = modelo.predict(x_test)

#Vendo a acurácia do meu modelo
from sklearn.metrics import confusion_matrix,classification_report
print(classification_report(y_test,resultado)) #Vejo que o meu modelo obteve resultados ruins
print(confusion_matrix(y_test,resultado))

#Para melhorar meu resultado, vou usar um grid search, para testar várias combinações de parâmetros, assim, com a finalidade de obter uma taxa de acerto maior
param_grid = {'C' : [0.1,1,10,100,1000], 'gamma' : [1,0.1,0.001,0.0001], 'kernel': ['rbf']}
from sklearn.model_selection import GridSearchCV

grid = GridSearchCV(SVC(),param_grid,refit = True, verbose = 3)
grid.fit(x_train,y_train)

#Verificando os melhores parametros encontrados
print(grid.best_params_)

#Tirando predições com esses grid
resultado_grid = grid.predict(x_test)
print(classification_report(y_test,resultado_grid)) #Vejo que o meu resultado foi bem superior
print(confusion_matrix(y_test,resultado_grid))
