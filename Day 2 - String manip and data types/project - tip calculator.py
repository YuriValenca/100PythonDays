print("Bem vindo à calculadora de gorjetas!")

valorConta = float(input("Começe nos dizendo qual foi o valor total da conta: "))

pctGorjeta = int(input("Quanto de gorjeta você(s) planeja(m) dar à casa? 10%, 12% ou 15%? "))

qntdPessoas = int(input("Massa! Obrigado! Quantas pessoas vão dividir a conta? "))

gorjeta = round(valorConta * (pctGorjeta/100), 2)

totalCada = round((gorjeta + valorConta)/qntdPessoas, 2)

message = f"A gorjeta total foi de R$ {gorjeta:.2f}, e cada pessoa deve pagar: R$ {totalCada:.2f}"

print(message)