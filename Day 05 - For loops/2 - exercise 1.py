# Calcular a altura média a partir de uma lista de entrada

alturasInput = input("Quais são as alturas?")

alturas = alturasInput.split(" ")

count = 0

for height in alturas:
    count += int(height)

avg = count/len(alturas)

print(f"A altura média é de {(avg/100):.2f}m")

# Outro possível método de "percorrer" a lista com o for é utilizando a função range, que recebe dois argumentos, geralmente o primeiro é 0, pois é o 1o elemento da lista, o último é, também geralmente, o tamanho da lista (se for definido) ou len(lista) se o tamanho da lista for desconhecido
# Outras funções que podiam ser utilizadas seriam sum(height), para somar todas as alturas e alocar em uma variável, e avg(sum), que tira a média (aritmética) de uma variável