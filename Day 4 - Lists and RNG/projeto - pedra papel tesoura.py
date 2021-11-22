import random

jogador = input("Pedra, papel ou tesoura? ")

maquina = random.randint(1, 3)

if maquina == 1:
    maquina = str("pedra")
elif maquina == 2:
    maquina = str("papel")
else:
    maquina = str ("tesoura")

print(f"A máquina escolheu {maquina}")

if jogador == maquina:
    print("Empate!")
elif jogador == "pedra" and maquina == "tesoura":
    print ("Você ganhou!")
elif jogador == "papel" and maquina == "pedra":
    print ("Você ganhou!")
elif jogador == "tesoura" and maquina == "papel":
    print ("Você ganhou!")
else:
    print("Você perdeu...")