#Vamos supor que fui contratado por uma empresa de comércio eletrônico.
#Essa empresa está tentando decidir se deve concentrar seu esforço em seu site ou em seu aplicativo móvel
#Portanto, vamos fazer análises e usar o modelo Linear Regression para determinar onde o esforço deve ser concentrado.
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

clientes = pd.read_csv("EcommerceCustomers.csv")

#Analisando o dataframe, vemos que possúi colunas de: Email, Endereço, Avatar, duração da sessão, tempo gasto no aplicativo, tempo gasto no site, quanto tempo o cliente é mebro, quantidade gasta anualmente
clientes.head()
clientes.info()

#Plotando alguns dados para tirar mais conclusões:
sns.jointplot(x = 'Time on Website', y = 'Yearly Amount Spent',data = clientes)
#Fazendo uma correlação entre o tempo gasto no site e a quantidade de dinheira gasta anualmente, vemos não é possível tirar uma conclusão sobre quanto mais tempo
#no site, mais dinheiro é gasto, uma vez que os dados parecem que estão dispostos de forma aleatória.

sns.jointplot(x = 'Time on App', y = 'Yearly Amount Spent',data = clientes) #Observo que para o aplicativo, é possível ver uma relação mais clara.
#Podemos ver uma relação linear entre o tempo gasto no app e a quantidade de dinheiro gasta anualmente

#Agora, comparando o tempo gasto no aplicativo e a duração da assosiação
#Ou seja, existe alguma relação entre tempo gasto no aplicativo e tempo de assosiação?
#Quanto mais tempo gasto no app, por mais tempo o cliente está associado? Ou o contrário?
sns.jointplot(x='Time on App', y = 'Length of Membership',kind = 'hex' ,data = clientes)
#Através da análise do gráfico gerado, se parece com o gráfico que relaciona tempo gasto no site e quantidade de dinheiro gasta anualmente.
#Ou seja, não existe uma relação clara entre tempo gasto no app e duração da assosiação, pois os dados parecem que estão distrubídos de forma aleatória.

#Agora, vou explorar melhor a relação para o conjunto de dados inteiros
sns.pairplot(clientes)
#Quanto ao gasto anualmente, percebo as relações lineares entre duração da sessão, tempo gasto no app (não no site), e duração da assosiação/tempo como mebro (sendo essa as relação mais forte).

#Para verificar melhor a relação entre tempo que a pessoa é membro e quantidade gasta analmente:
sns.lmplot(x='Length of Membership', y ='Yearly Amount Spent',data = clientes)

#Fazendo o treino de teste dos dados
x = clientes[['Avg. Session Length', 'Time on App','Time on Website', 'Length of Membership']]
y = clientes['Yearly Amount Spent']
#Vou tentar prever quanto meu cliente gastará, baseado naquelas 4 features

#Separando os dados de teste e de treinamento
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state = 101)

#Treinando o modelo, utilizando Linear Regression
from sklearn.linear_model import LinearRegression
modelo = LinearRegression()
modelo.fit(x_train,y_train)

print("Coeficientes: {}".format(modelo.coef_)) #Através da análise dos meu coeficientes, percebo que o a maior relação se dá
#entre duração da assosiação, como visto anteriormente. Percebo também, que a segunda relação que mais importa, é tempo no aplicativo.

#Fazendo a previsão dos dados
resultado = modelo.predict(x_test)

#Agora, vou verificar os valores reais x valores preditos
plt.scatter(y_test,resultado)
plt.xlabel('Dados Reais')
plt.ylabel('Valores preditos')
#visualmente, vejo que o meu modelo obteve resultados bem próximos aos reais.

#Avaliando melhor o meu modelo:
from sklearn import metrics

print('MAE:', metrics.mean_absolute_error(y_test, resultado))
print('MSE:', metrics.mean_squared_error(y_test, resultado))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, resultado))) #Vejo que o desvio padrão é de 8.9, ou seja, o modelo foi bom
#RMSE (Root Mean Squared Error) é o desvio padrão das distâncias entre a predição e os meus dados corretos.

sns.distplot(y_test-resultado) #Vejo que aproximadamente, tenho uma distrubuição normal.

#Tirando conclusões:
coeficientes = pd.DataFrame(modelo.coef_,x.columns)
coeficientes.columns = ['Coeficientes']
print(coeficientes)
#Vejo que, para o aumento de um minuto de sessão gasta com estilista, há um acréscimo de aproximadamente U$25.00
#Para o acréscimo de um minuto gasto de tempo no app, há um aumento de aproximadamente U$38.00
#Com a menor correlação, temos o tempo gasto no site e gasto anual, pois vejo que, o aumento de um minuto gasto no website, gera, aproximadamente U$0.19
#Por fim, com a maior correlação, temos a duração da assosiação. Para o aumento de uma unidade dessa feature, gera um aumento de, aproximadamente, U$61.00

#Pode-se inferir, portanto, que a maior receita provêm de clientes que estão a mais tempos fidelizados, seguidos por pessoas que passam mais tempo no app
#Ou seja, a empresa deve procurar formar de melhorar a captação de clientes que estão em seu site (transformar as pessoas que ficam navegando em seu site em futuros clientes)
#Visto que essa feature apresenta a menor correlação.
#A empresa também deve procurar mais formas de manter esse membro, visto que quanto mais tempo uma pessoa é mebro, mais ela tende a gastar.
