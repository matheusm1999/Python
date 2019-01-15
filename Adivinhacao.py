import random

def jogar ():
    print('='*35)
    print('Bem vindo ao jogo de adivinhação')
    print('='*35)

    numero_random = random.randrange(1,101) #gera um número aleatório entre 1 e 100
    #print(numero_random)
    total_de_tentativas = 3
    rodada = 1
    pontos = 1000


    print('Qual é o nível de dificuldade desejado? ')
    print('(1)Fácil (2)Médio (3)Difícil')
    nivel = int(input('Define o nível: '))


    while((nivel<1) or (nivel >3)):
        nivel = int(input('Digite um valor válido!! '))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    elif(nivel == 3):
        total_de_tentativas = 5


    #print('tt{}'.format(total_de_tentativas))

    while(rodada <= total_de_tentativas) :
        print("Tentativa: {} de {} ".format(rodada,total_de_tentativas))
        chute = int(input('Digite um valor entre 1 e 100: '))


        if(chute < 1 or chute > 100):
            print("Você deve digitar algum número entre 1 e 100!")
            continue #o continue faz sair dessa iteração, e assim, n quebra o meu laço

        acertou  = numero_random == chute
        maior    = chute > numero_random
        menor    = chute < numero_random

        if(acertou):
            print('Você acertou! Além disso, fez {} pontos'.format(pontos))
            break
        else:
            if(maior):
                print('Você errou! O seu chute foi maior que o número secreto')
            elif(menor):
                print('Você errou! O seu chute foi menor que o número secreto')
        rodada += 1
        pontos_perdidos = abs(numero_random - chute) #a distância entre meu número_aleatório e meu chute
        pontos -= pontos_perdidos #100 menos a distância entre meu número aleatório e meu chute

    print('Fim de jogo')

if (__name__ == "__main__"):
    jogar()
