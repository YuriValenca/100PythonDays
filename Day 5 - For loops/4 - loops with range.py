# Os loops de for não têm seu uso restrito apenas à listas, como visto anteriormente, pode ser utilizado aliando-se à função range(), onde ele irá percorrer a quantidade de números presentes entre os argumentos do range()

for number in range(1, 10):
    print(number)
print("\n")

# É possível ver que o print da função range não inclui o segundo argumento passado, apenas serão mostrados os número de 1 a 9

# Range() pode ainda receber outro argumento. Nota-se que o acréscimo de cada iteração é +1, o terceiro argumento serve justamente para modificar esse aumento. Analogamente, se passado um valor negativo (a depender de como os outros dois argumentos foram dados), é possível mostrar os número de forma decrescente

for number in range (1, 11, 2): #Começando do 1 e pulando de 2 em 2, esse comando irá imprimir todos os ímpares de 1 a 11, SEM INCLUIR o 11
    print(number)

print("\n")

for number in range (10, 1, -1):
    print(number)

count = 0

for number in range(1, 101):
    count += number

print(count)