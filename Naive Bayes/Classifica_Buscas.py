import csv
import pandas as pd #panda data analysis
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import AdaBoostClassifier


def carregar_busca():
    X = []
    Y = []

    arquivo = open('Cursos.csv','r')
    leitor = csv.reader(arquivo)
    next(leitor)

    for home,busca,logado,comprou in leitor:
        dados = [int(home),busca ,int(logado)]
        X.append(dados)
        Y.append(int(comprou))
    return X,Y


def fit_and_predict(nome,modelo,treino_dados,treino_marcacoes,teste_dados,teste_marcacoes):
    modelo.fit(treino_dados,treino_marcacoes)

    resultado = modelo.predict(teste_dados)

    diferencas = resultado - teste_marcacoes

    acertos = [diferenca for diferenca in diferencas if diferenca == 0]
    total_de_acertos = len(acertos)
    total_de_elementos = len(teste_dados)

    porcentagem_de_acertos = (total_de_acertos/total_de_elementos)*100.0
    print("O Algoritmo {} acertou {} de {}".format(nome,total_de_acertos,tamanho_de_teste))
    print("Em relação a porcentagem, o alagoritmo {} acertou {:.1f}%".format(nome,porcentagem_de_acertos))


#X,Y = carregar_busca() #não preciso dessa linha, logo, da função carregar_busca, pois estou usando o panads

df = pd.read_csv('C:/Users/mathe/OneDrive/Documentos/LABI/Python/Alura/MachineLearning/Cursos.csv') #data frame(df) são nossos dados
X_df = df[['home','busca','logado']]
Y_df = df['comprou']

Xdummies_df = pd.get_dummies(X_df)
Ydummies_df  = Y_df

#Transforma essas valores em uma array
X = Xdummies_df.values
Y = Ydummies_df.values

porcentagem_de_treino = 0.9

tamanho_de_treino = int(porcentagem_de_treino * len(Y))
tamanho_de_teste = len(Y) - tamanho_de_treino

treino_dados = X[:tamanho_de_treino]
treino_marcacoes = Y[:tamanho_de_treino]

teste_dados = X[-tamanho_de_teste:]
teste_marcacoes = Y[-tamanho_de_teste:]

#Começando agora a parte de Machine MachineLearning
#modelo = MultinomialNB()
modelo = AdaBoostClassifier()
fit_and_predict('AdaBoostClassifier',modelo,treino_dados,treino_marcacoes,teste_dados,teste_marcacoes)

modelo2 = MultinomialNB()
fit_and_predict('MultinomialNB',modelo2,treino_dados,treino_marcacoes,teste_dados,teste_marcacoes)

#Algortimo base que chuta tudo 0 ou 1
acerto_de_um = sum(teste_marcacoes)
#acerto_de_zero = acerto_de_um - Y
taxa_de_acerto_base = (acerto_de_um/len(teste_marcacoes) )*100
print("Taxa de acerto base:{}%". format(taxa_de_acerto_base))
