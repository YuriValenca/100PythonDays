import random

print("Bem vindo ao gerador de senhas!")

qtdLetras = int(input("Quantas letras você quer na sua senha? "))
qtdNumeros = int(input("Quantos números você quer na sua senha? "))
qtdSimbolos = int(input("Quantos símbolos você quer na sua senha? "))

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

simbolos = ['!', '#', '$', '%', '@', '%', '&', '*', '-', '+', '=']

senha = ""

for letter in range(qtdLetras):  # Range também aceita apenas um argumento, é como se existisse um 1o argumento "escondido", e ele é sempre = 0
    letraRandom = random.choice(letras)
    senha += letraRandom

for numero in range(qtdNumeros):
    numeroRandom = random.choice(numeros)
    senha += numeroRandom
    
for simbolo in range(qtdSimbolos):
    senha += random.choice(simbolos)  # É possível fazer as operações dos 2 for acima em apenas uma linha também

print(f"Que tal essa senha: {senha} ?")

# O método acima funciona, porém, a senha gerada segue um padrão, ela sempre vai ter primeiro as letras, depois os números e no fim os símbolos, então, é possível randomizar mais ainda a senha gerada! Uma das maneiras de fazer isso é juntando todos os caracteres em uma lista só, porém, os inputs n iam saber qual escolher, pois estariam todos na mesma lista, então não necessariamente, a senha seguirá o padrão pedido pelo usuário

senha2 = []

for letra in range(qtdLetras):
    senha2 += random.choice(letras)

for numero in range(qtdNumeros):
    senha2 += random.choice(numeros)

for simbolo in range(qtdSimbolos):
    senha2 += random.choice(simbolos)

# Podemos adicionar os caracteres, não a uma string, e sim a uma lista

random.shuffle(senha2)  # Para reorganizar uma lista, existe a função shuffle() do módulo random, que recebe como argumento a própria lista

senha2Str = ""
for i in senha2:
    senha2Str += i

print(f"É uma boa senha, mas essa aqui pode ser ainda mais segura: {senha2Str}")