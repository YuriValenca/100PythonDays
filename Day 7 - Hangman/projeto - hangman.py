import random

palavrasForca = []

f = open('C:\Portfólio\Python course\Day 7 - Hangman\ListaDePalavras.txt', 'r')

for line in f:
    palavrasForca.append(line.strip())

palavraSelecionada = random.choice(palavrasForca)

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
=========''',
 '''
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
    
print(f"Dica: a palavra escolhida tem {len(display)} letras!")

palpitesPassados = []   #Lista para guardar todos os inputs do usuário
palpitesRepetidos = []  #Lista para guardar os inputs repetidos e não punir o usuário por isso

vidas = 6

while vidas > 0 and '_' in display:

    palpite = input("Digite uma letra para ver se ela está na palavra: ").lower()
    
    if palpite in palpitesPassados:     # Se o input for repetido, colocar na lista de repetidos
        palpitesRepetidos.append(palpite)

    palpitesPassados.append(palpite)



    if palpite in palpitesRepetidos:    # Se o palpite for repetido, avisa ao usuário e não tira vida
        print(f"A letra {palpite.upper()} já foi escolhida")
    else:                               # Senão, continua os mesmos comandos do módulo anterior, para preencher a palavra

        if palpite in palavraSelecionada.lower(): 
            for i in range(len(palavraSelecionada)):
                letra = palavraSelecionada[i]
                if palpite == letra.lower():
                    display[i] = palpite

        else:
            print(f"Essa palavra não tem a letra {palpite.upper()}")
            vidas -= 1
    
    print(f"{' '.join(display)}")
    print(stages[vidas])     


# Se ao fim do loop while (que é a execução do jogo, vidas = 0, entra no segundo if, pois o usuário perdeu, se ele venceu (vidas > 0), primeiro if)

if vidas > 0:
    print(f"Venceu!! A palavra realmente era {palavraSelecionada}!")


if vidas == 0:
    print(f"Perdeu... A palavra era {palavraSelecionada}")