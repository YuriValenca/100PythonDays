# Programa para calcular compra de lata de tintas para pintar uma parede

import math   # Módulo do Python de matemática, útil para diversas coisas, nesse caso, nos dará a função ceil(), que arrendondará para cima uma divisão

areaTinta = 5   # Área que a tinta cobre (em m²)

alturaInput = int(input("Qual a altura da parede a ser pintada? "))
comprimentoInput = int(input("Qual o comprimento da parede a ser pintada? "))

def paintCalc(altura, comprimento, cobertura):
    numLatas = math.ceil((altura*comprimento)/cobertura)
    print(f"{numLatas} latas de tinta serão necessárias nessa pintura")

paintCalc(altura = alturaInput, comprimento = comprimentoInput, cobertura = areaTinta)
