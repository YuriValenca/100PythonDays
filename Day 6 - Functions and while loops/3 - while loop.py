# Outra estrutura de repetição existente é o while. Bastante similar ao for em usabilidade, porém as implementações são bem diferentes

algo = True

for item in range(10):
    # Faz algo
    print("oi")

while algo == True:
    # Faz algo repetidamente
    print("oi")
    algo == False  # No for, a condição de parada é dada no começo, com range() ou limitando ao número de itens numa lista, no while, a condição de parada fica dentro do bloco a ser repetido, caso não haja uma condição de parada, o código rodará pra sempre. Nesse caso, o bloco seria repetido apenas uma vez, pois assim que ele é executado, a variável algo vira False, e na comparação do while, a condição de repetição algo == True não é mais verdadeira, com isso, o bloco não é repetido de novo

# While loops são bastante usados quando não é sabido a quantidade de vezes que o bloco irá ser repetido, ou se a condição de parada se altera