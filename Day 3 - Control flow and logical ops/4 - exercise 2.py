# Calcular o IMC (BMI)
altura = (input("Qual sua altura em metros?: "))
peso = (input("Qual seu peso em kg?: "))

BMI = round(int(peso)/float(altura) ** 2, 1)

if BMI < 18.5:
    print (f"Seu IMC é de {BMI}, você está abaixo do peso, cuidado!")
elif BMI < 25:
    print (f"Seu IMC é de {BMI}, você está com peso normal :)")
elif BMI < 30:
    print (f"Seu IMC é de {BMI}, você está com sobrepeso. Te cuida, visse")
elif BMI < 35:
    print (f"Seu IMC é de {BMI}, você está com obesidade grau 1. Cuidado po...")
elif BMI < 40:
    print (f"Seu IMC é de {BMI}, você está com obesidade grau 2! Isso é ruim...")
else:
    print (f"Seu IMC é de {BMI}, você está com obesidade grau 3, ou mórbida! Isso é perigoso demais")

# Aqui, o que vale ressaltar é que não houve uso de operadores and para cercar um certo valor, por exemplo em peso normal, ao invés de BMI >= 18.5 and BMI < 25, isso só foi possível pois as condições estão em ordem crescente. Se a primeira condição fosse BMI < 40, a segunda BMI < 35 e assim por diante, só teríamos o bloco de obesidade grau 2 e mórbida sendo executados, isso porque, mesmo que o número se encaixasse em outra condicional, ele entrou PRIMEIRO na condição de < 35, sendo assim, o código executa essa condição primeiro. Para fazer as condições de maneiras decrescentes, aí sim seriam necessário cercar um intervalo (BMI >= 18.5 and BMI < 25 dessa maneira).