# Adicionar um país a mais, em formato de dicionário, na lista abaixo

diarioDeViagem = [
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

def addCountry(paisVisitado, cidadesVisitadas, nota):
    asdasd = 0
    # Primeiro passo deve ser criar um novo dicionário que servirá como o 3o elemento da lista diario de viagem:
    novoPais = {}
    # Em seguida, preenche-se o dicionário com as chaves presentes nos dicionários de diário de viagem:
    novoPais["país"] = paisVisitado
    novoPais["cidades visitadas"] = cidadesVisitadas
    novoPais["nota"] = nota
    diarioDeViagem.append(novoPais)
    


addCountry("EUA", ["Charleston", "St. Augustine", "Orlando"], 9)
print(diarioDeViagem)