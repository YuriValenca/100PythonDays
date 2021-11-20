# Projeto 3: Ilha do tesouro!
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')
print("Bem vindo à Ilha do Tesouro, explorador! Seu objetivo é achar esse maravilhoso tesouro acima. Ande pela ilha respondendo as perguntas com as opções que estão em aspas simples. A sua aventura começa numa bifurcação...")
decisao1 = input("Os caminhos da bifurcação parecem iguais... Qual você decide ir? 'Esquerda' ou 'Direita'?\n")

if decisao1 == 'esquerda':
    print("Após alguns minutos de caminhada, morcegos voam na sua cara e você se distrai, caindo em areia movediça... GAME OVER!")



else:
    print("Parece que você tomou a decisão correta... No fim do caminho, você se depara com um rio.")
    decisao2 = input ("Você quer 'nadar' o rio, 'esperar' algum barco passar ou 'procurar' algo que te ajude na travessia?\n")
    if decisao2 == 'esperar':
        print("Sua preguiça ou falta de ambição parecem ter te deixado na mão, você esperou muitas horas mas ainda há uma chance de achar o tesouro!")
        decisao21 = input("Você quer 'nadar' o rio ou 'procurar' algo que te ajude na travessia?\n")
        


    if decisao2 == 'nadar':
        print("É... isso era previsível... O rio está cheio de piranhas, não sobrou nem a alma pra contar a história... GAME OVER!")
        exit()
    else:
        print("Atrás de alguns arbustos, você encontra uma canoa! Sinal divino? Algo que o último aventureiro usou? Não interessa agora... Você conseguiu atravessar o rio!")
        decisao3 = input("A entrada do templo do tesouro e seu interior estranhamento foram bem tranquilos. Porém, você tem uma importante decisão agora... Qual porta você escolhe, 'amarela', 'azul' ou 'verde'?\n")
        if decisao3 == 'azul':
            print("A porta tranca atrás de você e o caminho te leva ao exterior do templo, pra uma enorme cachoeira, não há saída, só se sobreviver a queda... GAME OVER!")
            exit()
        elif decisao3 == 'verde':
            print("A porta tranca atrás de você e o caminho te leva a um grande lago dentro do templo, porém, ele está infestado de crocodilos... GAME OVER!")
            exit()
        else:
            print("A porta tranca atrás de você, o caminho escuro te leva a um grande salão, onde um enorme baú aguarda para ser looteado... VOCÊ VENCEU!")