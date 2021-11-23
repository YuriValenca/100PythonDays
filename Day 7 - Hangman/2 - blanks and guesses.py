# Nessa etapa do desafio, cada caracter da palavra será trocado por "_", correspondendo ao formato da forca original, além disso, já será possível substituir o "_" pelo input (correto) do usuário. Será necessário, antes, colar aqui parte do módulo anterior para novamente criar uma lista a partir do txt.

import random

palavrasForca = []

f = open('C:\Portfólio\Python course\Day 7 - Hangman\ListaDePalavras.txt', 'r')

for line in f:
    palavrasForca.append(line.strip())

palavraSelecionada = random.choice(palavrasForca)

print(palavraSelecionada)

palpite = input("Digite uma letra para ver se ela está na palavra: ").lower()

display = ['_'] * len(palavraSelecionada)

# for letra in palavraSelecionada:      Um jeito de fazer com que apareça na tela os _ para cada letra é com o for, mas o jeito mais rápido e prático é multiplicando diretamente no display a quantidade de letras (len()) da palavra selecionada
#     display.append("_")

for i in range(len(palavraSelecionada)):    # Esse for diz basicamente que, para cada posição da palavra selecionada, verificar se o palpite é igual à letra da posição atual, se for,
    letra = palavraSelecionada[i]           # já troca o display de _ para a letra correta, se não, deixa como está
    if palpite == letra.lower():
        display[i] = palpite

print(display)