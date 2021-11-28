# Verificador de números primos

def verificadorPrimo(numero):
    ehPrimo = True
    for i in range(2, numero):
        if numero % i == 0:
            ehPrimo = False
    if ehPrimo:    # Se a verificação de um if for uma condição booleana e verdadeira, no caso, ehPrimo == True, ela pode ser simplificada para conter só a variável a ser checada, como é o caso aqui
        print("É primo!")
    else:
        print("Não é primo.")

n = int(input("Qual número deve ser verificado? "))
verificadorPrimo(numero = n)