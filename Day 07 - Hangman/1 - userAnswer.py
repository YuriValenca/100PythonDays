import random

palavrasForca = []

# Em prol de melhorar a experiência do jogo, baixei um arquivo com uma lista de palavras em português. No entando, isso requereu que fosse utilizado uma propriedade ainda não vista e que não será atacada nessa lição da forca: o open file. Assim que esse conteúdo for mencionado no curso, eu modificarei esse código para referir onde está a teoria por trás do bloco de código abaixo. Mas é bom saber que ele serve para identificar cada palavra do arquivo e colocá-las numa lista, separando cada uma pelo "\n", operação que quem faz é o line.strip(). O for irá percorrer o arquivo e sair armazenando cada palavra numa lista vazia, que será a utilizada no jogo da forca final

f = open('C:\Portfólio\Python course\Day 7 - Hangman\ListaDePalavras.txt', 'r')

for line in f:
    palavrasForca.append(line.strip())

palavraSelecionada = random.choice(palavrasForca)

print(palavraSelecionada)

letraUser = input("Digite uma letra para ver se ela está na palavra: ")

for letra in palavraSelecionada:
    if letraUser.lower() == letra.lower():
        print("True")
    else:
        print("False")
    
# Essa parte do desafio confere, além da existência da letra na palavra, onde ela está, substituindo pelo output "True", o resto vira "False"