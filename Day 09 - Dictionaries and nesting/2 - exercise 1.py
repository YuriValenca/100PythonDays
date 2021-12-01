# Alocar os valores da prova dos estudantes para notas

estudantes = {
    "Harry" : 81,
    "Ron" : 78,
    "Hermione" : 99,
    "Draco" : 74,
    "Neville" : 62,
}

notas = {

}

for nota in estudantes:     # For para percorrer o dicionário estudantes
    resultado = estudantes[nota]        #Alocação do VALOR de cada termo do dicionário na variável resultado
    if resultado > 90:      # Checagem do valor, para definir qual termo vai ser adicionado ao novo dicionário e com que valor respectivo ele irá
        notas[nota] = "A"
    elif resultado > 80:
        notas[nota] = "B"
    elif resultado > 70:
        notas[nota] = "C"
    elif resultado > 60:
        notas[nota] = "D"
    else:
        notas[nota] = "F"

print(notas)