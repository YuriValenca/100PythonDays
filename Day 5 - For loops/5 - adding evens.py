# Calcular soma dos numeros pares de 1 a 100

count = 0
for number in range(2, 101, 2): #Se começar de 1, ele vai pegar todos os ímpares!! O arg 1 do range() tem que ser 2 (ou 0)
    count += number

print(count)

# Outro método:

count2 = 0
for number in range(1, 101):
    if number % 2 == 0:
        count2 += number
    
print(count2)