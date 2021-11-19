# Calcular o IMC (BMI)
altura = (input("Qual sua altura em metros?: "))
peso = (input("Qual seu peso em kg?: "))

BMI = int(peso)/float(altura) ** 2

print("Seu IMC é: " + str(BMI))