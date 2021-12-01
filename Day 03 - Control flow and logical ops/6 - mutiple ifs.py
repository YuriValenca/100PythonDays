print("Bem vindo à montanha-russa!")
altura = float(input("Qual sua altura? "))

total = 0   #A criação dessa variável com valor 0 é importante pois ela está fora do escopo de onde será usada. O 0 serve para determinar o tipo da variável, pois, se criamos ela vazia, o tipo dela, por default seria string. Seria, sim, possível inicializar essa variável dentro da função, ou do bloco de código condicional, nesse caso, porém, não seria possível utilizar essa variável fora dele se fosse feito isso.

if altura > 1.2:
    print("Você pode andar na montanha-russa!")
    idade = int(input("Para continuar a compra do seu ingresso, nos diga qual sua idade: "))
    if idade > 18:
        print("O valor do ingresso é 12 reais")
        total = 12
    elif idade > 12:
        print("O valor do ingresso é 7 reais")
        total = 7
    else:
        print("O valor do ingresso é 5 reais")
        total = 5
    
    foto = input("Você vai querer que a gente tire fotos suas? ")

    if foto == "sim" or foto == "s" or foto == "SIM" or foto == "S":
        print("Legal! As fotos vão ficar ótimas")
        total += 3
    else:
        print("Tudo bem. Aproveite o passeio!")
    
    print(f"O total a ser pago é de R$ {total:.2f}")

else:
    print("Você não tem altura pra ir na montanha-russa...")