#Classificando emails em diferentes categorias 
import pandas as pd
from sklearn.model_selection import cross_val_score
from collections import Counter
import numpy as np
import nltk

#Processos de limpeza dos textos:
#Stop words;
#Extrair as raízes das palavras;
#Separar as palavras de uma frase usando o tokenize;
#Remover palavras com pontuações do dicionário.

classificacoes = pd.read_csv('emails.csv',encoding = 'utf-8')
#print(classificacoes.head()) #Vejo que tenho duas colunas, a coluna email e a coluna classificacao
textos_puros = classificacoes['email']
#print(textos_puros)

#Quero transformar isso em um dicionário. Para isso, vou começar quebrando a frase de acordo com os espaços em brancos
frases = textos_puros.str.lower() #transformo todas as palavra em minúsculas e depois quebro a frase
textos_quebrados = [nltk.tokenize.word_tokenize(frase) for frase in frases ]# Separo entre espaços em brancos e pontos, transformando em uma lista de lista
#print(textos_quebrados) #Vejo que é uma lista de listas


#usando stopwordsa para reduzir o ruído dos meus dados e focar apenas nos dados (palavras) que revelam algo de útil

#nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words("portuguese")

#Pegando apenas a raíz das palavras, uma vez que palavras como: aluno,aluna,alunos,alunas são a mesma coisa
stemmer = nltk.stem.RSLPStemmer()

#Colocando todas as palavras em um conjunto. Dessa forma, não tenho elementos (palavras) repetidas
dicionario = set()
for lista in textos_quebrados: #passo por cada lista de textos_quebrados
    palavras_validas = [stemmer.stem(palavra) for palavra in lista if palavra not in stopwords and len(palavra) > 2] #passo por cada palavra de lista, e adiciono no meu dicinário seu não for stopword e se o tamanho da palavra for maior que 2
    dicionario.update(palavras_validas)

#print(dicionario)
total_de_palavras = len(dicionario)
#print(total_de_palavras)

tuplas = zip(dicionario, range(total_de_palavras)) #Agora, cada palavra está seguida de um número, que indica sua posição
#transformando em um dicinário
dicionario = {palavra:indice for palavra,indice in tuplas}
#print(dicionario)
#Agora posso também fazer consultas desse tipo:
#print('posição da palavra pode {}'.format(dicionario['pode']))

#Agora, para cada palavra que aparece na frase, localizo ela no dicinário e acrescento em um, para assim saber quantas vezes essa palavra apareceu
#Entrada: texto que será vetorizado e dicionário de palavras, onde essa palavra está contida
#Saída: texto vetorizado (acrescenta em 1 na posicão daquela palavra)
#Pré condição: A palavra precisa estar no dicinário
def vetorizar_texto(texto,dicionario):
    vetor = [0]*len(dicionario)
    for palavra in texto:
        if len(palavra) > 0: #se o tamanho da palavra for maior que 0
            raiz = stemmer.stem(palavra) #Pego a raíz
            if raiz in dicionario: #se essa raíz estiver no dicinário
                posicao = dicionario[raiz]
                vetor[posicao] += 1 #somo 1 nessa posição
    return vetor

vetores_de_texto = [vetorizar_texto(texto,dicionario) for texto in textos_quebrados] #Agora, para cada frase, tenho um array do tamanho do meu dicinário
#print(vetores_de_texto)

#Dividindo entre variáveis de teste e treino
x = np.array(vetores_de_texto)
y = np.array(classificacoes['classificacao'].tolist())
porcentagem_de_treino = 0.8
tamanho_do_treino = int(porcentagem_de_treino *len(y))
tamanho_da_validacao = len(y) - tamanho_do_treino

treino_dados = x[0:tamanho_do_treino]
treino_marcacoes = y[0:tamanho_do_treino]

validacao_dados = x[tamanho_do_treino:]
validacao_marcacoes = y[tamanho_do_treino:]


def fit_and_predict(nome, modelo, treino_dados, treino_marcacoes):
    k = 10
    scores = cross_val_score(modelo, treino_dados, treino_marcacoes, cv = k)
    taxa_de_acerto = np.mean(scores)
    msg = "Taxa de acerto do {}: {}".format(nome, taxa_de_acerto)
    print(msg)
    return taxa_de_acerto

def teste_real(modelo, validacao_dados, validacao_marcacoes):
    resultado = modelo.predict(validacao_dados)

    acertos = resultado == validacao_marcacoes

    total_de_acertos = sum(acertos)
    total_de_elementos = len(validacao_marcacoes)

    taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos

    msg = "Taxa de acerto do vencedor entre os dois algoritmos no mundo real: {0}".format(taxa_de_acerto)
    print(msg)

resultados = {}

#Usando diversos algorítmos para checar o resultado
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
modeloOneVsRest = OneVsRestClassifier(LinearSVC(random_state = 0))
resultadoOneVsRest = fit_and_predict("OneVsRest", modeloOneVsRest, treino_dados, treino_marcacoes)
resultados[resultadoOneVsRest] = modeloOneVsRest

from sklearn.multiclass import OneVsOneClassifier
modeloOneVsOne = OneVsOneClassifier(LinearSVC(random_state = 0))
resultadoOneVsOne = fit_and_predict("OneVsOne", modeloOneVsOne, treino_dados, treino_marcacoes)
resultados[resultadoOneVsOne] = modeloOneVsOne

from sklearn.naive_bayes import MultinomialNB
modeloMultinomial = MultinomialNB()
resultadoMultinomial = fit_and_predict("MultinomialNB", modeloMultinomial, treino_dados, treino_marcacoes)
resultados[resultadoMultinomial] = modeloMultinomial

from sklearn.ensemble import AdaBoostClassifier
modeloAdaBoost = AdaBoostClassifier(random_state=0)
resultadoAdaBoost = fit_and_predict("AdaBoostClassifier", modeloAdaBoost, treino_dados, treino_marcacoes)
resultados[resultadoAdaBoost] = modeloAdaBoost

print(resultados)

#Verificando qual foi obteve o melhor desempenho
maximo = max(resultados)
vencedor = resultados[maximo]

print("Vencerdor: ")
print(vencedor)

vencedor.fit(treino_dados, treino_marcacoes)

teste_real(vencedor, validacao_dados, validacao_marcacoes)

acerto_base = max(Counter(validacao_marcacoes).values())
taxa_de_acerto_base = 100.0 * acerto_base / len(validacao_marcacoes)
print("Taxa de acerto base: %f" % taxa_de_acerto_base)

total_de_elementos = len(validacao_dados)
print("Total de teste: %d" % total_de_elementos)
