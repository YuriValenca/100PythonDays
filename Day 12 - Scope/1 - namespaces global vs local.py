enemies = 1

def increaseEnemies():
    # A mudança da variável de 1 pra 2 foi feita DENTRO da função, então, o compilador entende que o único lugar que essa variável deve ficar alterada é dentro dessa função, fora dela, a variável vale 1 para todos que forem acessá-la, dentro de incresceEnemies(), vale 2
    enemies = 2
    print(f"Inimigos dentro da função: {enemies}")

increaseEnemies()
print(f"Inimigos fora da função: {enemies}")

def drinkPotion():
    potionStrength = 2
    print(potionStrength)

# Nesse caso, a variável foi criada dentro da função, então lá, é o único lugar q ela pode ser acessada e/ou modificada. É dito que o escopo de potionStrength é LOCAL, o escopo de enemies é GLOBAL
drinkPotion()
# print(potion_Strength)

# Python, no entanto, diferentemente de Java ou C++, não tem escopo de bloco:

if 3 > 2:
    novaVariavelGlobal = 10

# Blocos como if/elif/else não contam como "cercas" de escopo, ou delimitadores, ou seja, as variáveis criadas neles são GLOBAIS