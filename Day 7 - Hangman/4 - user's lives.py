# Nesta parte, será possível lidar com uma letra errada do usuário

import random

palavrasForca = []

f = open('C:\Portfólio\Python course\Day 7 - Hangman\ListaDePalavras.txt', 'r')

for line in f:
    palavrasForca.append(line.strip())

palavraSelecionada = random.choice(palavrasForca)

print(palavraSelecionada)

# A lista abaixo serve para mostrar ao usuário o quão perto ele está de perder, desenhando na tela o homem na forca

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

display = ['_'] * len(palavraSelecionada)

for i in range(len(palavraSelecionada)): 
    letra = palavraSelecionada[i]
    if letra == '-':
        display[i] = '-'

print(display)

vidas = 6

while vidas > 0 and '_' in display:     # A codição de parada agora será se o usuário ainda tiver vidas E se ainda existem '_' na palavra (ou seja, se ainda existem letras a serem colocadas)

    palpite = input("Digite uma letra para ver se ela está na palavra: ").lower()

    if palpite in palavraSelecionada.lower():       # Se o palpite estiver presente na palavra, percorre ela para substituir '_' pela letra
        for i in range(len(palavraSelecionada)):
            letra = palavraSelecionada[i]
            if palpite == letra.lower():
                display[i] = palpite
    else:                                           # Se não, perde uma vida
        vidas -= 1
    print(display)
    print(stages[vidas])

if '_' not in display:
    print("Venceu!!")

if vidas == 0:
    print(f"Perdeu... A palavra era {palavraSelecionada}") 