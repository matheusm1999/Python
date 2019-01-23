import pandas as pd


base = pd.read_csv('C:/Users/mathe/OneDrive/Documentos/LABI/Python/MachineLearning/risco-credito.csv')

#Separando entre previsores e classe
previsores =base.iloc[:,0:4].values#Pegando todas as linhas, e as colunas 0, 1, 2, 3
classe = base.iloc[:,4].values #Minha classe é a minha última coluna (número 4)

#Entretanto, possui variáveis categóricas, logo foi transformá-las em variáveis numéricas
from sklearn.preprocessing import LabelEncoder
Labelencoder = LabelEncoder()
previsores[:,0] = Labelencoder.fit_transform(previsores[:,0])
previsores[:,1] = Labelencoder.fit_transform(previsores[:,1])
previsores[:,2] = Labelencoder.fit_transform(previsores[:,2])
previsores[:,3] = Labelencoder.fit_transform(previsores[:,3])

from sklearn.naive_bayes import GaussianNB
classificador = GaussianNB()
classificador.fit(previsores,classe)

#Valores que minha classe pode assumir: Alto,Moderado,Baixo
#Vou adicionar um dado com as seguintes características:
#História = Boa
#Dívida = Alta
#Garantias = Nenhuma
#Renda = >35
resultado = classificador.predict([[0,0,1,2] , [3,0,0,0]])
print(resultado) #Observo que para o meu segundo dado, que possúi 3 valores iguais a 0, a minha correção Laplaciana já é feita
#Ou sejam adiciona tantos regristros quantos forem necessários até que esse problema com valores iguais a 0 seja resolvido, uma vez que esse valor específico acaba interferindo
#No cálculo que o algorítmo Naive Bayes faz
