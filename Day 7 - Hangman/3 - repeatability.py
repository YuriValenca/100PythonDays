# Essa parte do desafio pretende atacar a repetibilidade do jogo, que é um dos pilares da forca: o usuário coloca letras até ganhar ou perder.

import random

palavrasForca = []

f = open('C:\Portfólio\Python course\Day 7 - Hangman\ListaDePalavras.txt', 'r')

for line in f:
    palavrasForca.append(line.strip())

palavraSelecionada = random.choice(palavrasForca)       # Novamente criando a lista e selecionando uma palavra dela

print(palavraSelecionada)

display = ['_'] * len(palavraSelecionada)

for i in range(len(palavraSelecionada)):        # Verificação da existência do caracter - já que ele está presente em alguma palavras, decidi que era melhor revelá-lo, para não 
    letra = palavraSelecionada[i]               # confundir o usuário e para que os inputs dele sejam apenas letras, e que não seja preciso adivinhar símbolos
    if letra == '-':
        display[i] = '-'

print(display)

# Enquanto o display ainda possuir '_', vai significar que ainda existem letras a serem colcoadas na palavra, então, o usuário deve continuar tentando acertar a palavra. Quando não existirem mais '_', a condição de parada do while (while '_' in display) torna-se falsa, e o loop para

while '_' in display:

    palpite = input("Digite uma letra para ver se ela está na palavra: ").lower()   #Pedindo repetidas vezes o palpite do usuário

    for i in range(len(palavraSelecionada)):        # Laço for utilizado no módulo passado, para trocar o '_' no display pela letra, caso ela exista na palavra
        letra = palavraSelecionada[i]
        if palpite == letra.lower():
            display[i] = palpite
    print(display)                              # Print do estado atual da palavra, toda vez que uma letra é colocada

if '_' not in display:
    print("Venceu!!")