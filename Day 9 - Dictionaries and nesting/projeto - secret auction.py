import os
cls = lambda: os.system('cls')

# O código acima servirá para limparmos o console após a inserção de um nome e valor, afim de manter certa "veracidade" no leilão secreto

lances = {

}

leilaoTerminado = False

def maiorLance(historicoDeLances):
    lanceAlto = 0
    vencedor = ""
    for ofertador in historicoDeLances:
        valorOfertado = historicoDeLances[ofertador]
        if valorOfertado > lanceAlto:
            lanceAlto = valorOfertado
            vencedor = ofertador
    print(f"O vencedor foi {vencedor}, com um lance de R$ {lanceAlto:.2f}")

while not leilaoTerminado:      # Ou while leilaoTerminado == False
    nome = input("Qual seu nome? ")
    preco = int(input("Quanto é o seu lance? R$ "))
    lances[nome] = preco
    deveContinuar = input("Existem outras pessoas para dar algum lance? Digite 's' ou 'n' ")
    if deveContinuar == 'n':
        leilaoTerminado = True      #Termina o laço quando não existirem mais apostadores
        maiorLance(lances)
    elif deveContinuar == 's':
        cls()       # Chama a função de limpar o console se ainda tiverem apostadores