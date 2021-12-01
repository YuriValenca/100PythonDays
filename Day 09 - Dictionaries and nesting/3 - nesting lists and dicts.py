# Aninhar dicionários e listas é possível em Python, basta que um valor de um termo, ao invés de ser "único", ele seja uma lista, ou ainda, um dicionário (com mais aninhamentos dentro)

# Uma chave tem apenas um valor no dicionário, por isso que aninhamento com listas é importante, para que, se necessário, possamos alocar mais de um valor a uma chave

diarioDeViagem = {
    "França" : ["Paris", "Lille", "Lyon"],
    "Alemanha" : "Munique",
    "EUA" : ["Charleston", "St. Augustine", "Orlando"]
}

# A propósito, é possível aninhar uma lista em outra lista! O código abaixo é totalmente válido (embora seja, geralmente, menos utilizável na prática)

lista = ['a', 'b', ['c', 'd']]

# Aninhando tudo agora!

diarioDeViagem2 = {
    "França" : 
    { "cidades visitadas" : 
        ["Paris", "Lille", "Lyon"],
        "Nota do país" : 10,    
    },
    "Alemanha" : "Munique",
    "EUA" : ["Charleston", "St. Augustine", "Orlando"]
}

# O termo França tem valor de um outro dicionário, com termo cidades visitadas, que por sua vez, tem como valor uma lista de cidades. A identação e a sintaxe é oq mais deve receber atenção aqui, pois vários sinais e símbolos podem se misturar

# Para evitar aninhamentos extremamente confusos, o melhor a se fazer é que dois (ou mais) dicionários sejam elementos de uma lista:

diarioDeViagem3 = [
    {
        "país" : "França",
        "cidades visitadas" : ["Paris", "Lille", "Lyon"],
        "nota" : 10
    },
    {
        "país" : "Alemanha",
        "cidades visitadas" : ["Munique"],
        "nota" : 7
    },
]