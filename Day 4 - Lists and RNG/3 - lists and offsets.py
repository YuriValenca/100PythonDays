# Lista é uma das muitas estruturas de dados presentes na computação. Estrutura de dados (ou data struct) é um jeito organizado é agil de armazenar informações no código. Até agora, apenas armazenou-se dados nas variáveis, porém, cada variável só tem capacidade de armazenar um valor, tornando inviável uma escalabilidade de muitos dados consecutivos. Nisso, as listas auxiliam bastante

# Além da quantidade, dados presentes em data structs muito geralmente tem uma relação, ou uma ordem. O padrão de uma lista é: [item1, item2, ...]

estadosEUA = ["Delaware", "Pennsylvnia", "Hawaii"] # É possível também aliar uma lista (e seu conteúdo) a uma variável, para reutilizar a lista durante o código e poder operá-la. Vale ressaltar que a ordem de uma lista é dada pela ordem dos elementos colocados nela (lembrando que sempre começa em 0!), nesse caso estadosEUA[0] = "Delaware", estadosEUA[1] = "Pennsylvania", e assim por diante. Por outro lado, um índice negativo irá percorrer a lista do fim ao começo: estadosEua[-1] = "Hawaii"

estadosEUA[1] = "Pensilvânia" # Editando o valor de um elemento da lista

# Cada vez que uma lista é criada, diversas funções do Python podem ser utilizadas para modificar a lista de alguma forma. Para adicionar um elemento ao fim da lista, utiliza-se a função append("elemento a ser adicionado")

estadosEUA.append("New Jersey")

# Por outro lado, adicionar um elemento a uma determinada posição é pela função index(), que recebe dois parâmetros, a posição a ser colocado (deslocando para a direita os elementos subsequentes) e o elemento a ser adicionado

estadosEUA.insert(2, "Georgia")
print(estadosEUA)

# Para colocar múltiplos elementos no fim (como se fosse um loop de append), Python tem a função extend

estadosEUA.extend(["South Carolina, North Carolina"])
print(estadosEUA)