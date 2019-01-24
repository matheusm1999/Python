#Usando o algorítmo Naive Bayes para saber se uma determinada pessoa pagou ou não um empréstimo

import pandas as pd

base = pd.read_csv("C:/Users/mathe/OneDrive/Documentos/LABI/Python/MachineLearning/credit-data.csv")
#base.describe()

#base.loc[base['age'] < 0] # Vejo que tenho 3 idades menores que 0

#Vou substituir esses valores que estão negativos pela média dos dados
#Entretanto, não vou considerar esses valores negativos.
media = base['age'][base.age > 0].mean() #faço a média apenas dos valores maiores que 0
#print (media)

#Agora, substituto pela média
base.loc[base.age < 0,'age'] = media

#print(base.loc[base['age'] < 0]) #Agora não tenho nenhum valor negativo

#Agora, vou verificar se existe algum atributo sem nenhum valor
#print(base.loc[pd.isnull(base['age'])]) #3 idades vazias

#Vou separar meus atributos previsores da variável dependente
previsores = base.iloc[:,1:4].values #Pego todas as linhas (primeiro :), e pego a coluna 1 até a 4, ou seja, ignoro a coluna "clientid"
#pois é uma chave primária. Deixo a minha coluna "default" de fora, pois é a minha classe (vai do 1 até o 3)

classe = base.iloc[:,4].values
#print(classe)


from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean',axis = 0)
imputer = imputer.fit(previsores[:,1:4])
previsores[:,1:4] = imputer.transform(previsores[:,1:4])
#print(previsores) #Posso perceber a diferença de valores entre a coluna 0 e 1, por isso, vou fazer um escalonamento

#Escalonando
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)
#print(previsores) #Agoro posso perceber que não existe um valor grande entre a coluna 0 (renda) e 1 (idade)

#Por fim, agora faço a divisão dos dados de treino e teste
from sklearn.model_selection import train_test_split
previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores,classe,test_size = 0.25,random_state = 0)

#Usando o algorítmo Naive Bayes
from sklearn.naive_bayes import GaussianNB
classificador = GaussianNB()
classificador.fit(previsores_treinamento,classe_treinamento)
resultado = classificador.predict(previsores_teste)

#Agora, vou testar a acurácia do meu modelo
from sklearn.metrics import confusion_matrix, accuracy_score
precisao = accuracy_score(classe_teste, resultado)
print('O algoritmo teve uma taxa de acerto de {}%'.format(precisao*100))
matriz = confusion_matrix(classe_teste,resultado)
total_acertos = matriz[0][0] + matriz[1][1]
total_erros = matriz[0][1] + matriz[1][0]
print(matriz)
print('Portanto, o algoritmo acertou {} e errou {} da classe 0 '.format(matriz[0][0],matriz[0][1]))
print('Quanto a classe 1, o algortimo acertou {} e errou {}'.format(matriz[1][1],matriz[1][0]))
print('Logo, o total de acertos foram: {}'.format(total_acertos))
print('Já o total de erros foram de : {}'.format(total_erros))
print('A quantidade total de dados para o teste eram de: {}'.format(len(classe_teste)))
