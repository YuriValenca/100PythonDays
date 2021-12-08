# Projeto de jogo para acertar um número randomizado de 1 a 100

import random

num = random.randint(1, 100)    #randomizando um número de 1 a 100

TENTATIVAS = 10         # Vidas = 10, como base, se a dificuldade for 'dificil', as vidas são cortadas pela metade
venceu = False

dificuldade = input("Escolha a dificuldade do jogo: Digite 'facil' ou 'dificil' ")

def jogo(vidas):
    """Função que recebe o número de tentativas de acordo com a dificuldade e verifica o palpite do usuário, sinalizando se está alto, baixo ou se ele acertou."""
    palpite = int(input("Digite seu palpite: \n"))
    if palpite > num:
        mensagem = "Muito alto"
    elif palpite < num:
        mensagem = "Muito baixo"
    else:
        mensagem = "Acertou! Você venceu!"
    return mensagem

if dificuldade == 'dificil':        # Jogo com 5 tentativas
    TENTATIVAS -= 5
    while TENTATIVAS > 0 and venceu == False:
        output = jogo(vidas = TENTATIVAS)
        print (output)

        if output != "Acertou! Você venceu!":
            TENTATIVAS -= 1
            print(f"Você ainda tem {TENTATIVAS} tentativas.\n")
        else:
            venceu = True
else:       # Prossegue o jogo com 10 tentativas
    while TENTATIVAS > 0 and venceu == False:
        output = jogo(vidas = TENTATIVAS)
        print (output)
        if output != "Acertou! Você venceu!":
            TENTATIVAS -= 1
            print(f"Você ainda tem {TENTATIVAS} tentativas.\n")
        else:
            venceu = True

if venceu == False:     # Revela ao usuário qual era o número, caso ele não vença o jogo
    print(f"Você não conseguiu adivinhar o número... O número sorteado foi: {num}")