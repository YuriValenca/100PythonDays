# Calculadora de tempo de vida restante, com base numa expectativa de vida de 90 anos:
age = int(input("Digite sua idade: "))

anosRestantes = 90 - age
mesesRestantes = anosRestantes * 12
semanasRestantes = anosRestantes*52
diasRestantes = semanasRestantes * 7

message = f"Você tem {anosRestantes} anos restantes de vida, isso dá um total de {mesesRestantes} meses, que são {semanasRestantes} semanas, ou ainda {diasRestantes} dias."

print(message)
# F strings não precisam necessariamente estar contidas no print, é possível colocar dentro de uma variável!