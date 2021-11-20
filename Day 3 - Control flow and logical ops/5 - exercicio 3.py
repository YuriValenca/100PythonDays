# Verificador de ano bissexto (Leap Year)

ano = int(input("Digite o ano que você quer checar se é bissexto ou não: "))

if ano % 4 == 0:
    if ano % 100 == 0 and ano % 400 == 0:   #Se for divisível por 4, 100 e 400, é bissexto
        print("Ano bissexto")
    elif ano % 100 == 0 and ano % 400 != 0: #Se for divisível por 4 e 100, não é
        print("Ano não bissexto")
    else:
        print("Ano bissexto")   #Essa checagem funciona pois o ano é divisível por 4 e já foi feita a checagem de erro da divisão por 100 e 400, então, mesmo que não seja divisível pelos 2, se for por 4 ja é bissexto
else:
    print("Ano não bissexto")   #Se falhar a divisão por 4, ja não é

# Um ano será bissexto se for divisível por 4. Além disso, se ele for divisível por 4, 100 E por 400, ele também é bissexto, por essa razão que anos como 2100, 1700 ou 2500 não são bissextos, pois falham em ser divisíveis por 400. O código acima abraça todas essas restrições por meio de condições aninhadas. Outra maneira de fazer:

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print ("Ano bissexto")  #Se for divisível por 100, entra no condicional aninhado para checar se é divisível por 400, se for, é bissexto
        else:
            print ("Ano não bissexto")  #Se não, falha a checagem do erro, e não é ano bissexto
    else:
        print("Ano bissexto")   #Se não for divisível por 100, mas for por 4, automaticamente é bissexto
else:
    print("Ano não bissexto")   #Se nem divisível por 4 ele for, já falha