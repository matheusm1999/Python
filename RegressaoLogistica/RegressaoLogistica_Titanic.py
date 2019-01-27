#Análise do acidente do Titanic
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline

train = pd.read_csv("RegressaoLogistica/titanic_train.csv")

print(train.head())

print(train.info())#ao todo, tenho 891 entradas

#Fazendo o pre-processamento de dados
print(train.isnull()) #Vejo que tenho daldos faltantes

plt.figure(figsize=(12,6))
sns.heatmap(train.isnull(),yticklabels='false',cmap = 'viridis') #Podemos ver melhor os elementos faltantes dessa forma
#E assim, percebo que a coluna "cabin" possúi vários dados faltantes.
#ALém disso, a coluna "Age", possúi cerca de 30% de valores faltantes

#Vou ver agora os passageiros que sobreviveram, pelo sexo
sns.countplot(x='Survived',hue = 'Sex',data = train)
#Percebo que a maiora das pessoas que morreram, foram homens, e a maniora da pessoas que sobreviveram, foram mulheres

#Agora, vejo quais os passageiros que sobreviveram, de acordo com a classe dos mesmos
sns.countplot(x='Survived',hue = 'Pclass',data = train)#Vejo que a maiora das pessoas que não sobreviveram foram da classe 3

#Olhando a destribuição de idade dos passageiros no titanic
train['Age'].hist()#A maiora dos passageiros eram jovens(entre 20 e 30 anos), pelo que podemos observar. 

sns.countplot(x='SibSp',data = train) #Verifico agora a quantidade de passageiros que estavam ou não acompanhados
#Vejo que a maioria não estava acompanhado. Os que estavam, tinham, em sua maioria, uma pessoa junto consigo.

train[train['SibSp'] == 0 ]['Age'].hist() #Vejo a idade dos passageiros que não estavam acompanhados. Percebo a queda que ocorre conforme as idades são menores
#Uma vez que crianças não entraram sozinhas

train['Fare'].hist(bins=50,figsize=(12,6)) #Observo agora o valor pago pela passagem, vejo que a maioria dos passageiros pagou menos de U$100.00

train[train['Fare']<70]['Fare'].hist(bins=50,figsize=(12,6)) #Dando um "Zoom" na minha figura acima

#Agora, vou fazer o tratamento dos meus dados
#Tentando fazer alguma estratégia para o preenchimento dos dados faltantes.
plt.figure(figsize=(12,6))
sns.boxplot(x='Pclass',y='Age',data = train)#Vejo que a média dos passageiros da classe 1,2,3 são, respectivamente:  37,29,24 anos

#Vou preencher os dados faltantes da coluna idade pela média da idade de cada classe
#Entrada: Data Frame com duas colunas que quero trabalhar, "age" e "Pclass"
#Saída: Caso o valor esteja faltando, é retornado a média de idade para a classe da qual o passageiro pertence. Se não estiver com o falor faltando, retorna a própria idade do passageiro
#Pré condição: Passeiro precisa ter valor válido na coluna "Pclass"
#Pós condição: Passageiro com idade faltante, substituída pela média da idade da sua respectiva classe
def preencher_idades(coluna):
    idade = coluna[0]
    classe = coluna[1]
    
    if pd.isnull(idade):
        if classe == 1:
            return 37
        elif classe == 2:
            return 29
        else:
            return 24
    else:
        return idade
    
train['Age'] = train[['Age','Pclass']].apply(preencher_idades,axis=1)

#Verificando agora a coluna "Age"
sns.heatmap(train.isnull(),yticklabels='false',cmap = 'viridis') #Percebo que agora não há mais dados faltantes na coluna "Age"

#Como a coluna "Cabin" possúi vários valores faltantes, vou deletar a coluna inteira
del train['Cabin']
#Verificando, vejo que a minha coluna "Cabin" desapareceu
sns.heatmap(train.isnull(),yticklabels='false',cmap = 'viridis')

#Na minha coluna "Embarked", tenho um valor nulo. Por ser apenas um valor nulo, vou deletá-lo
train.dropna(inplace = True)
#Verificando novamente
sns.heatmap(train.isnull(),yticklabels='false',cmap = 'viridis')

#Agora, preciso mudar minhas variáveis nominais para numéricas.
#Começando pela coluna "Sex"
sex = pd.get_dummies(train['Sex'], drop_first = True)

#Agora, para a coluna "Embarked"
embark = pd.get_dummies(train['Embarked'],drop_first = True)
print(embark)

#Agora, posso remover umas colunas, como por exemplo a coluna nome e ticket, que não terão importância para o meu modelo
#Também vou excluir a coluna "Sex" e substituir pela que criei anteriormente
train.drop(['Sex','PassengerId','Name','Ticket','Embarked'],axis = 1,inplace = True)
print(train.head())

train = pd.concat([train,sex,embark],axis = 1)
print(train.head(50))

#Agora, fazendo o treinamento do modelo
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

#Fazendo o modelo que dirá se o passageiro sobreviveu ou não
x_train,x_test,y_train,y_test = train_test_split(train.drop('Survived',axis = 1),train['Survived'],test_size = 0.3)

#Treinando e aplicando meu modelo
modelo = LogisticRegression()
modelo.fit(x_train,y_train)
resultado = modelo.predict(x_test)

#Verificando a acurácia do meu modelo
from sklearn.metrics import classification_report
print(classification_report(y_test,resultado))
#Vejo que meu modelo acertou 81% dos casos, portanto, um bom modelo
