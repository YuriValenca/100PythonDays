# Imprimir números de 1 a 100. Se for divisível por 3, printar "fizz", se for por 5, "buzz", se for pelos 2, "fizzbuzz"

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)