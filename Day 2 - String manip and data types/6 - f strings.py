print(round(8/3)) #A função round recebe um ou dois parâmetros para arredondar uma variável ou operação. Se receber um param, o número será arredondado para um int, se receber dois, o número será arredondado para um float e o segundo parâmetro determinará a quantidade de casas decimais a serem printadas
print(round(8/3, 2))

# Toda divisão que o Python faz, mesmo que seja uma sem resto, resulta em um tipo float de dado. É possível transformar uma divisão em int utilizando a abreviação da função floor:
print (8 // 3)

# Lembrando que python não possui a capacidade de entender ++ ou --, escreve-se então +=, -=, /= e *=

# F Strings: para facilitar o print e evitar muitos casts, é possível misturar um print de string com int a partir do seguinte formato:

score = 1000
altura = 1.76
eVerdade = True

print(f"Seu score é {score}, sua altura é {altura}, é {eVerdade} que você é bonito")
# Lembrar de colocar o f DENTRO do print, mas ANTES das aspas (simples ou duplas), as variáveis têm de ser colocadas dentro de chaves {}, com isso, o Python ja faz o cast direto, e o print aceita qualquer tipo de dado