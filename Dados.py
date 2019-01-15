import csv
from sklearn.naive_bayes import MultinomialNB

def carregar_acesso():
    X  = []
    Y = []



    arquivo =  open("C:/Users/mathe/OneDrive/Documentos/LABI/Python/Alura/MachineLearning/acesso.csv","r")  #abre o meu arquivo .cs
    leitor = csv.reader(arquivo) #le arquivos .csv (arquivos de estatística)
    next(leitor) #ignora a primeira linha

    for home,como_funciona,contato,comprou in leitor:
        dado  = [int(home),int(como_funciona),int(contato)]
        X.append(dado)
        Y.append(int(comprou)) #adiciono meu resultado aqui, meu 'y'
    return X,Y



X,Y = carregar_acesso()

treino_dados = X[:90]
treino_marcacoes = Y[:90]

teste_dados = X[-9:]
teste_marcacoes = Y[-9:]

modelo = MultinomialNB()
modelo.fit(treino_dados,treino_marcacoes)
#print(modelo.predict(teste))
resultado = modelo.predict(teste_dados)
diferencas = resultado - teste_marcacoes
acertos = [diferenca for diferenca in diferencas if diferenca == 0]
total_de_acertos = len(acertos)
total_de_elementos = len(teste_dados)
porcentagem_de_acertos = (total_de_acertos/total_de_elementos)*100.0
print("Acertou {} de {}".format (total_de_acertos,total_de_elementos ))
print("{:.0f}% de acerto".format(porcentagem_de_acertos) )
