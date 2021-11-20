# Programa de calculadora do amor!

nome1 = nome2 = ''

nome1 = input("Qual o seu nome? ").lower()
nome2 = input("Qual o nome do seu amor? ").lower()

TCount = nome1.count('t') + nome2.count('t') 
RCount = nome1.count('r') + nome2.count('r')
UCount = nome1.count('u') + nome2.count('u')
ECount = nome1.count('e') + nome2.count('e')
LCount = nome1.count('l') + nome2.count('l')
OCount = nome1.count('o') + nome2.count('o')
VCount = nome1.count('v') + nome2.count('v')

trueCount = 10*(TCount + RCount + UCount + ECount)
lovCount = LCount + OCount + VCount + ECount

compat = trueCount + lovCount

print(f"Sua compatibilidade com seu amor é de {compat}%.")

if compat <= 10 or compat >= 90:
    print("Vocês combinam como Coca cola e mentos")
elif compat >=40 and compat <= 50:
    print("Vocês até que combinam :)")
else:
    print("Boa sorte com ela!")