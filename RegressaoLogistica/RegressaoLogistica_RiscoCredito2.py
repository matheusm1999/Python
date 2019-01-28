import pandas as pd

base = pd.read_csv('C:/Users/mathe/OneDrive/Documentos/LABI/Python/MachineLearning/risco-credito2.csv')

#Separando entre variáveis peditoras e classe
previsores = base.iloc[:,0:4].values
classe = base.iloc[:,4].values

print(base.head())

#Transformando variáveis categóricas em variáveis numéricas
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
previsores[:,0] = labelencoder.fit_transform(previsores[:,0])
previsores[:,1] = labelencoder.fit_transform(previsores[:,1])
previsores[:,2] = labelencoder.fit_transform(previsores[:,2])
previsores[:,3] = labelencoder.fit_transform(previsores[:,3])

print(base.head())#Vejo a diferença agora, com as variáveis sendo transformada em numéricas

#Treinando de aplicando meu modelo
from sklearn.linear_model import LogisticRegression
classificador = LogisticRegression()
classificador.fit(previsores,classe)
#Vendo os coeficientes de cada atributo
print(classificador.intercept_)
print(classificador.coef_)

#Predizendo o resultado
#Valores que minha classe pode assumir: Alto,Moderado,Baixo
#Vou adicionar um dado com as seguintes características:
#História = Boa
#Dívida = Alta
#Garantias = Nenhuma
#Renda = >35
resultado = classificador.predict([[0,0,1,2] , [3,0,0,0]])
#Posso ver também, o resultado das probabilidades
resultado2 = classificador.predict_proba([[0,0,1,2] , [3,0,0,0]])
print("Resultado: {}".format(resultado))
print("Probabilidade do meu primeiro dado ser da classe alto: {:.2f}%".format(resultado2[0][0]*100))
print("Probabilidade do meu primeiro dado ser da classe baixo: {:.2f}%".format(resultado2[0][1]*100))
print("Probabilidade do meu segundo dado ser da classe alto: {:.2f}%".format(resultado2[1][0]*100))
print("Probabilidade do meu segundo dado ser da classe alto: {:.2f}%".format(resultado2[1][1]*100))
