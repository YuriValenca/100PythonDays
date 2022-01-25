# Para simplificação do projeto:
# O deck tem tamanho infinito;
# Não tem Joker;
# Valete, rainha e rei valem 10;
# Ás vale 1 ou 11;
# As cartas possuem a mesma probabilidade de serem sorteadas;
# As cartas não são "removidas" do deck quando "puxadas".

import random

cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

querJogar = input("Aceita jogar uma partida de BlackJack? 's' para jogar ou 'n' para sair ")


# FUNÇÕES
def puxaCarta():
    cartaPuxada = random.choice(cartas)
    return cartaPuxada

def calculaValor(deck):
    """Pega uma lista de cartas e retorna o valor, checando inclusive, se há um Blackjack com 2 cartas e, ainda, se o Ás deve valer 1 ou 11"""
    if sum(deck) == 21 and len(deck) == 2:
        return 0
    if 11 in deck and sum(deck) > 21:
        deck.remove(11)
        deck.append(1)
    return sum(deck)


# Vale notar que é impossível haver mais de 1 return dessa função, isso porque o if/elif/else é avaliado de cima pra baixo, então se, por exemplo, a 3a condição é verdadeira e há um return, a função já para ali
def vencedor(scoreDealer, scoreJogador):
    if scoreDealer ==  scoreJogador:
        return "Empate"
    elif scoreDealer == 0:
        return "Dealer tem um Blackjack, você perdeu!"
    elif scoreJogador == 0:
        return "Você tem um Blackjack, ganhou!"
    elif scoreJogador > 21:
        return "Passou de 21, perdeu"
    elif scoreDealer > 21:
        return "Dealer passou de 21, você ganhou"
    elif scoreJogador > scoreDealer:
        return "Você tem o placar maior, ganhou!"
    else:
        return "Dealer tem o placar maior, você perdeu"

if querJogar == 's':
    cartasJogador = []
    cartasDealer = []
    gameOver = False

    # Randomiza 2 cartas pro jogador

    cartasJogador.append(puxaCarta())
    cartasJogador.append(puxaCarta())

    # Randomiza 2 cartas pro dealer

    cartasDealer.append(puxaCarta())
    cartasDealer.append(puxaCarta())


    while not gameOver:

        scoreJogador = calculaValor(deck = cartasJogador)
        print(f"Suas cartas: {cartasJogador}, valor das cartas: {scoreJogador}")

        scoreDealer = calculaValor(deck = cartasDealer)
        print(f"Primeira carta do dealer: {cartasDealer[0]}\n")

        if scoreJogador == 0 or scoreDealer == 0 or scoreDealer > 21 or scoreJogador > 21:
            gameOver = True
        else:
            continuaJogando = input("Digite 's' para pegar outra carta ou 'n' para revelar o deck do Dealer: \n")
            if continuaJogando == 's':
                if scoreDealer < 17 and scoreDealer != 0:
                    cartasDealer.append(puxaCarta())
                cartasJogador.append(puxaCarta())
            else:
                gameOver = True

    scoreJogador = calculaValor(deck = cartasJogador)
    print(f"Sua mão final foi: {cartasJogador}, valor dessas cartas: {scoreJogador}\n")
    scoreDealer = calculaValor(deck = cartasDealer)
    print(f"As cartas do Dealer eram: {cartasDealer}, valor das cartas: {scoreDealer}\n") 
    print(vencedor(scoreDealer, scoreJogador))