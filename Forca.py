from random import randrange


def imprime_mensagem_abertura():
    print ("="*30)
    print("Bem vindo ao jogo da forca!!")
    print("="*30)

def carega_palavra_secreta():
    arquivo = open("palavra.txt","r")
    palavras = []

    for linha in arquivo: #le linha por linha em um arquivo
        linha = linha.strip() #tiro os espaços em branco
        palavras.append(linha) #adiciono a minha palavra na lista palavras

    arquivo.close() #SEMPRE FECHAR O ARQUIVO

    numero_aleatorio = randrange(0,len(palavras))
    palavra_secreta = palavras[numero_aleatorio].upper() #vai sortear uma palavra na posicao numero_aleatorio
    return palavra_secreta

def inicializa_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta] #vai ter um "_" para cada letra em "Palavra_secreta"

def pede_chute():
    chute = input("Qual a letra? ")
    chute = chute.strip().upper() #tira os espaços no início e no fim
    return chute

def marca_chute_correto(palavra_secreta,chute,letras_acertadas):
     index = 0 #guarda a posição da letra, pois vou precisar depois
     for letra in palavra_secreta: #Percorre minha string "Palavra_secreta" letra por letra
         if(chute == letra ): #se meu chute for igual a letra (uma vez q letra está em "Palavra_secreta")
             letras_acertadas[index] = letra #Minha String, na posição [index], recebe a letra, caso seja igual ao chute
         index += 1 #atualizo meu indice

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def jogar ():
    imprime_mensagem_abertura()
    palavra_secreta = carega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    #Variáveis que são usadas para meu while, que ocorrerá enquanto ambas foram False
    enforcou = False
    acertou = False

    erros = 0


    print(letras_acertadas)

    while(not enforcou and not acertou):
         chute = pede_chute()

         if(chute in palavra_secreta):  #se existe o minha letra chutada na minha String "Palavra_secreta"
            marca_chute_correto(palavra_secreta,chute,letras_acertadas)
         else:
             erros += 1 #se não tiver, Errou, logo, atualizado minha variável erro
             desenha_forca(erros)
             #print("Você errou! Faltam {} tentativas".format(6-erros))

         enforcou = erros == 7 # enforcou recebe true se erros for = 6
         acertou = "_" not in letras_acertadas #se não tiver "_" em letras acertadas, acaba o jogo
         print(letras_acertadas) #imprime a minha String "letras_acertadas", com a nova letra, caso seja correta, ou não


    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)
    print("Fim de jogo!")

if (__name__ == "__main__"):
        jogar()
