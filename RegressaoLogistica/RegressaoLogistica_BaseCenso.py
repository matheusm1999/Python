import pandas as pd

base = pd.read_csv("census.csv")

#base.describe()
#base.head() #Percebo que tenho tanto variáveis numéricas quanto categóricas, logo vou transformar tudo em numérico

#Primeiro passo, vou dividir os meus atributos preditores da minha classe
previsores = base.iloc[:,0:14].values
classe = base.iloc[:,14].values

#Agora, transformo os atributos categóricos em numéricos
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder_previsores = LabelEncoder()
previsores[:,1] = labelencoder_previsores.fit_transform(previsores[:,1])
previsores[:,3] = labelencoder_previsores.fit_transform(previsores[:,3])
previsores[:,5] = labelencoder_previsores.fit_transform(previsores[:,5])
previsores[:,6] = labelencoder_previsores.fit_transform(previsores[:,6])
previsores[:,7] = labelencoder_previsores.fit_transform(previsores[:,7])
previsores[:,8] = labelencoder_previsores.fit_transform(previsores[:,8])
previsores[:,9] = labelencoder_previsores.fit_transform(previsores[:,9])
previsores[:,13] = labelencoder_previsores.fit_transform(previsores[:,13])

#Agora, preciso transformar meus atributos nominais em dummyes, pois são características, e não faz sentido eles terem algum peso
#O que afetaria meus algorítimos de ML

onehotencoder = OneHotEncoder(categorical_features = [1,3,5,6,7,8,9,13])
previsores = onehotencoder.fit_transform(previsores).toarray()

#Agora, vou fazero escalonamento
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)

#Por fim, agora faço a divisão dos dados de treino e teste
from sklearn.model_selection import train_test_split
previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores,classe,test_size = 0.15,random_state = 0)

#Usando o Naive bayes
from sklearn.linear_model import LogisticRegression
classificador = LogisticRegression()
classificador.fit(previsores,classe)
resultado = classificador.predict(previsores_teste)

from sklearn.metrics import confusion_matrix,accuracy_score
precisao = accuracy_score(classe_teste,resultado)
print("O modelo teve uma taxa de acerto de {}%".format(precisao*100)) #Se executar o modelo usando o OneHotEncoder e o escalonamento, vejo que o meu resultado é de 85% de acerto.
#Portanto, vou executar o modelo novamente, mas sem esse pré-processamento (apenas o escalonamento e a transformações dos atributos nominais para numéricos, para o algorítmo funcionar)
#E assim vejo que o meu resultado é de 82%
#Executando agora, o OneHotEncoder, sem o escalonamento, vejo que meu resutlado é de 80%
#Nesse caso, o pré-processamento (OneHotEncoder e o escalonamento) fez com que os resultados fossem maiores, quase o dobro do resultado do Naive bayes (que foi de 47%), com o mesmo pré-processamento

matriz = confusion_matrix(classe_teste,resultado)
print(matriz)
