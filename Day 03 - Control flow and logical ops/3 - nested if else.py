print("Bem vindo à montanha-russa!")
altura = float(input("Qual sua altura? "))

if altura > 1.2:
    print("Você pode andar na montanha-russa!")
    idade = int(input("Para continuar a compra do seu ingresso, nos diga qual sua idade: "))
    if idade > 18:      
        #Essa é uma condição aninhada, ela só será executada se o bloco dentro do if exterior for verdadeiro, se o condicional externo for para o bloco de códigos do "else", nada do que está dentro do if externo seria executado, INCLUINDO o if/else aninhado.
        print("O valor do ingresso é 12 reais")
    elif idade > 12 and idade <= 18:     
        #O condicional elif serve para que o else/if não seja apenas binário, múltiplos elifs podem ser invocados à medida que o código necessite de mútiplas condições diferentes
        print("O valor do ingresso é 7 reais")
    else:
        print("O valor do ingresso é 5 reais")
else:
    print("Você não tem altura pra ir na montanha-russa...")

# Por fim, lembrar que dentro das condições dos blocos, é possível que seja necessário juntar duas ou mais condições, como ocorreu na linha 9, para isso, o Python dispõe de operadores lógicos como and, or e not