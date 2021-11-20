# Programa para preço de pizza!

print("Bem vindo à Python Pizzeria!")
tamanho = input("Qual tamanho você deseja? ")
pepperoniBool = input("Deseja pepperoni extra? ")
queijoBool = input("Deseja queijo extra? ")
precoPizza = 0
tamanhoPizza = ''

# Preço do tamanho:
if tamanho == "p":
    precoPizza += 15
    tamanhoPizza = 'p'
elif tamanho == "m":
    precoPizza += 20
    tamanhoPizza = 'm'
else:
    precoPizza += 25
    tamanhoPizza = 'g'

# Preço do pepperoni:
if pepperoniBool == "s":
    if tamanhoPizza == 'p':
        precoPizza += 2
    else:
        precoPizza += 3

# Preço do queijo:
if queijoBool == "s":
    precoPizza += 1

print(f"O preço total da pizza foi de R$ {precoPizza},00")

# Existem diversas maneiras de realizar esse código, aqui, preferi separar a precificação de cada item pedido para o usuário, ao invés de aninhar várias condicionais (embora ainda haja aninhamento)
