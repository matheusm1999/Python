import pandas as pd
import numpy as np
from math import sqrt

class Usuario:
    def __init__(self,user_id):
        self.user_id = user_id
        self.lista_de_filmes = []
        self.lista_de_avaliacoes = []
        self.f = 0


    def __lt__(self, other):
        return self.f < other.f

    #Cria um filme e avalia esse filme
    #Entrada: filme que será inserido na lista de filme e nota desse filme
    def criar_avaliar_filme(self,id_filme,nota):
        self.lista_de_filmes.append(id_filme)
        #print('id {} adicionado'.format(id_filme))
        self.lista_de_avaliacoes.append(nota)
        #print('nota {} adicionada'.format(nota))

    #Calculo a distancia euclidiana/similaridade entre meu usuário e os todos os outros
    def distancia_euclidiana(self,usuario2):
        #pego o primeiro filme do usuario_novo e faço menos o primeiro filme do usuario2
        quantidade_de_usuarios = 0
        posicao_usuario = 0
        posicao_filme = 1
        quantidade_de_filmes_avaliados = 1

        diferenca = 0
        distancia = 0
        soma_das_diferencas = 0
        lista_de_distancias = []

        while(quantidade_de_usuarios != len(usuario2)): #Percorro a lista de usuário
            #print('len da lista: {}'.format(len(usuario2)))
            #print('qutd {}'.format(quantidade_de_usuarios))
            while(quantidade_de_filmes_avaliados < len(usuario2[posicao_usuario].lista_de_avaliacoes)): #Entro na lista de avaliações de cada usuário - enquanto não acabarem os filmes avaliados
                if(self.lista_de_avaliacoes[posicao_filme] != 0 and usuario2[quantidade_de_usuarios].lista_de_avaliacoes[posicao_filme] != 0): #calculo a distancia euclidiana se a minha avaliacao for diferente de zero
                    #print('qtd filmes avaliados {}'.format(quantidade_de_filmes_avaliados))
                    #print('qtd lista de avaliacoes {}'.format(len(usuario2[posicao_usuario].lista_de_avaliacoes)))
                    diferenca = self.lista_de_avaliacoes[posicao_filme] - usuario2[posicao_usuario].lista_de_avaliacoes[posicao_filme]
                    soma_das_diferencas += diferenca * diferenca #faço a soma dessas diferenças e elevo ao quadrado
                    #print("Avaliando o usuario {} e o usuario {}:".format(self.user_id,usuario2[posicao_usuario].user_id))

                    #print('Filme do usuario1: {}'.format(self.lista_de_filmes[posicao_filme]))
                    #print('Filme do usuario2: {} '.format(usuario2[posicao_usuario].lista_de_filmes[posicao_filme]))

                    #print('Nota do filme do usuario1: {}'.format(self.lista_de_avaliacoes[posicao_filme]))
                    #print('Nota do filme do usuario2: {}'.format(usuario2[posicao_usuario].lista_de_avaliacoes[posicao_filme]))
                    #print('difenreca calculada: entre pontos {} e {} = {}'.format(self.lista_de_avaliacoes[posicao_filme],usuario2[posicao_usuario].lista_de_avaliacoes[posicao_filme],diferenca))
                    #print('soma das diferencas: {}'.format(soma_das_diferencas))
                    #print('\n')

                    #print("O filme f'{self.lista_de_filmes[posicao_filme]} do usuarios {} e o filme {} do usuario {} tiveram notas, respectivamentes de : {} e {}".format(self.lista_de_filmes[posicao_filme],self.user_id,usuario2[posicao_usuario],self.lista_de_avaliacoes[],usuario2[posicao_usuario].lista_de_filmes[posicao_filme],))

                    #print("O filme {} do usuarios {} e o filme {} do usuario {} tiveram notas, respectivamentes de : {} e {}".format(self.lista_de_filmes[posicao_filme],self.user_id,usuario2[posicao_usuario],self.lista_de_avaliacoes[],usuario2[posicao_usuario].lista_de_filmes[posicao_filme],))
                    #print("Portanto, a sua distancia eh de: {}")
                quantidade_de_filmes_avaliados+=1
                posicao_filme+=1

            distancia = 1 / (1 + (sqrt(soma_das_diferencas)) )
            lista_de_distancias.append(distancia)
            soma_das_diferencas = 0
            #distancia = np.sqr
            posicao_filme = 1
            quantidade_de_filmes_avaliados = 1
            quantidade_de_usuarios+=1
            posicao_usuario+=1
            print('valor adicionado na lista: {}'.format(distancia))

        return lista_de_distancias

    def vizinho_mais_proximo(self,k,lista_de_distancias,lista_de_usuarios):
        lista_de_distancias_ordenada = []
        lista_de_usuarios_ordenada = []

        posicao = 0

        lista_de_distancias_ordenada_final = []
        lista_de_usuarios_ordenada_final = []
        #return lista_de_distancias_ordenadas,lista_de_usuarios_ordenada = (lista(t) for t in zip(*sorted(zip(lista_de_distancias,lista_de_usuarios))))
        lista_de_distancias_ordenada, lista_de_usuarios_ordenada =(list(t) for t in  zip(*sorted(zip(lista_de_distancias, lista_de_usuarios))))
        lista_de_distancias_ordenada_final = list(reversed(lista_de_distancias_ordenada))
        lista_de_usuarios_ordenada_final = list(reversed(lista_de_usuarios_ordenada))
        #return lista1, lista2
        #Agora que ordenei a minha lista, vou pegar os meus k vizinhos mais proximos
        soma_dos_pesos = 0

        for i in range(0,4):
            soma_dos_pesos += lista_de_distancias_ordenada_final[i]

        soma_das_lista_peso = 0
        media_ponderada = 0
        posicao_filme_nao_avaliado = 0
        posicao_usuario = 0

        while(posicao_filme_nao_avaliado != len(self.lista_de_avaliacoes)):
         #Verifico cada usuario
            if(self.lista_de_avaliacoes[posicao_filme_nao_avaliado] == 0): #vou ver se esse filme foi avaliado, se não for
                while(posicao_usuario != k ):
                    soma_das_lista_peso += lista_de_usuarios_ordenada_final[posicao_usuario].lista_de_avaliacoes[posicao_filme_nao_avaliado] *lista_de_distancias_ordenada_final[posicao_usuario]
                    #while(self.lista_de_avaliacoes[posicao_filme_nao_avaliado] != len(self.lista_de_avaliacoes)): #vou ver quais os filmes nao avaliados
                     #se esse filme nao tiver sido avaliado
                    #então, vou fazer uma avaliação para esse posição
                    media_ponderada = soma_das_lista_peso/soma_dos_pesos
                    self.lista_de_avaliacoes[posicao_filme_nao_avaliado] = media_ponderada
                    print('O filme {} tera uma possivel nota de : {}'.format(self.lista_de_filmes[posicao_filme_nao_avaliado],self.lista_de_avaliacoes[posicao_filme_nao_avaliado]))
                    posicao_usuario += 1
            posicao_filme_nao_avaliado+=1
            soma_das_lista_peso = 0
            posicao_usuario = 0
        #posicao_filme_nao_avaliado += 1







#Criando usuários
usuario1 = Usuario(1)
usuario2 = Usuario(2)
usuario3 = Usuario(3)
usuario4 = Usuario(4)
usuario5 = Usuario(5)
usuario6 = Usuario(6)
usuario7 = Usuario(7)
usuario8 = Usuario(8)

#Esse será meu usuário novo, o qual não terá avaliado alguns filmes
usuario_novo = Usuario(9)


lista_de_usuarios = []
lista_de_usuarios.append(usuario1)
lista_de_usuarios.append(usuario2)
lista_de_usuarios.append(usuario3)
lista_de_usuarios.append(usuario4)
lista_de_usuarios.append(usuario5)
lista_de_usuarios.append(usuario6)
lista_de_usuarios.append(usuario7)
lista_de_usuarios.append(usuario8)



#print('id do usuario: {}'.format(usuario1.user_id))
#Criando filmes e dando notas para esses filmes
usuario1.criar_avaliar_filme(1,5)
usuario1.criar_avaliar_filme(2,3)
usuario1.criar_avaliar_filme(3,5)
usuario1.criar_avaliar_filme(4,4)
usuario1.criar_avaliar_filme(5,2)
usuario1.criar_avaliar_filme(6,5)

usuario2.criar_avaliar_filme(1,3)
usuario2.criar_avaliar_filme(2,2)
usuario2.criar_avaliar_filme(3,5)
usuario2.criar_avaliar_filme(4,3)
usuario2.criar_avaliar_filme(5,5)
usuario2.criar_avaliar_filme(6,5)

usuario3.criar_avaliar_filme(1,1)
usuario3.criar_avaliar_filme(2,1)
usuario3.criar_avaliar_filme(3,4)
usuario3.criar_avaliar_filme(4,4)
usuario3.criar_avaliar_filme(5,5)
usuario3.criar_avaliar_filme(6,1)

usuario4.criar_avaliar_filme(1,3)
usuario4.criar_avaliar_filme(2,3)
usuario4.criar_avaliar_filme(3,3)
usuario4.criar_avaliar_filme(4,5)
usuario4.criar_avaliar_filme(5,5)
usuario4.criar_avaliar_filme(6,2)

usuario6.criar_avaliar_filme(1,2)
usuario6.criar_avaliar_filme(2,3)
usuario6.criar_avaliar_filme(3,5)
usuario6.criar_avaliar_filme(4,4)
usuario6.criar_avaliar_filme(5,4)
usuario6.criar_avaliar_filme(6,5)

usuario7.criar_avaliar_filme(1,2)
usuario7.criar_avaliar_filme(2,4)
usuario7.criar_avaliar_filme(3,4)
usuario7.criar_avaliar_filme(4,4)
usuario7.criar_avaliar_filme(5,4)
usuario7.criar_avaliar_filme(6,5)

usuario8.criar_avaliar_filme(1,5)
usuario8.criar_avaliar_filme(2,2)
usuario8.criar_avaliar_filme(3,3)
usuario8.criar_avaliar_filme(4,1)
usuario8.criar_avaliar_filme(5,4)
usuario8.criar_avaliar_filme(6,3)

usuario5.criar_avaliar_filme(1,2)
usuario5.criar_avaliar_filme(2,4)
usuario5.criar_avaliar_filme(3,2)
usuario5.criar_avaliar_filme(4,3)
usuario5.criar_avaliar_filme(5,3)
usuario5.criar_avaliar_filme(6,5)

usuario_novo.criar_avaliar_filme(1,0) #0 indica que o mesmo não avaliou o primeiro filme
usuario_novo.criar_avaliar_filme(2,4)
usuario_novo.criar_avaliar_filme(3,2)
usuario_novo.criar_avaliar_filme(4,3)
usuario_novo.criar_avaliar_filme(5,0)
usuario_novo.criar_avaliar_filme(6,5)


lista_de_usuarios_ordenada = []
lista_de_distancias_ordenada = []

lista_de_distancias = usuario_novo.distancia_euclidiana(lista_de_usuarios)#Calculo a distancia euclidiana desse usuário para todos os outros

#print(distancia)
usuario_novo.vizinho_mais_proximo(3,lista_de_distancias,lista_de_usuarios)
#print('filme {} com nota: {}'.format(usuario1.lista_de_filmes,usuario1.lista_de_avaliacoes))
#print(lista_de_distancias_ordenadas)
