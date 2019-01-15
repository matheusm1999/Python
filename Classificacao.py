from sklearn.naive_bayes import MultinomialNB
#naive_bayes é uma biblioteca de sklearn, e MultinomialNB é um algoritmo que usarei pra treinar meu modelo

#é gordo? tem perna curta? late?
porco = [1,1,0]
porco2 = [1,1,0]
porco3 = [1,1,0]
cachorro1 = [1,1,1]
cachorro2 = [0,1,1]
cachorro3 = [0,1,1]

dados = [porco,porco2,porco3,cachorro1,cachorro2,cachorro3]

marcacoes = [1,1,1,-1,-1,-1] #minhas marcações, ou seja: Se for 1, é porco, se for -1, é cachorro.

misterioso1 = [1,1,1] #eh gordo, tem perna curta e late, logo eh porco ou cachorro? tem que dar -1
misterioso2 = [1,0,0] #tem que dar 1, pois é porco
misterioso3 = [0,0,1]
testes = [misterioso1, misterioso2,misterioso3]
marcacoes_teste = [-1,1,-1]

total_de_elementos = len(testes)

modelo = MultinomialNB()
modelo.fit(dados,marcacoes)
resultado = modelo.predict(testes) #chuta se é porco(1) ou cachorro (-1)
print(resultado)

diferencas = resultado - marcacoes_teste #Tenho uma lista em "diferenca", que contém o chute/resultado do computador. Em marcacoes_teste, tenho a minha resposta correta, e assim comparo com a do computador
acertos = [diferenca for diferenca in diferencas if diferenca == 0] #guardo os meus valores iguais a 0, ou seja, os meus acertos
total_de_acertos = len(acertos) #minha variavel total_de_acertos é criada recebendo a quantidade de acertos.
#Essa conta funciona da seguinte forma:
#se o valor era 1 e foi chutado 1 a conta será: 1 - 1 = 0 (logo, acertou)
#Se o valor era 1 e foi chutado -1 a conta será: 1 - (-1) = 2 (logo, errou)
#Se o valor era -1 e foi chutado 1 a conta será -1 - 1 = -2 (logo, errou)
#Se o valor era -1 e foi chutado -1, a conta será -1 - (-1) = 0 (logo, acertou)
print("Acertou {} de {} elementos" .format(total_de_acertos,total_de_elementos))

taxa_de_acertos = (total_de_acertos/total_de_elementos) *100.0
print("Taxa de acerto: {:.0f}%".format(taxa_de_acertos))
