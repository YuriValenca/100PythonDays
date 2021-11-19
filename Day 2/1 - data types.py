# Data types

# Strings (ou textos)
print("Oi!"[2]) #O índice presente dentro dos colchetes indica para o programa que ele deve printar apenas o caracter presente nesse índice, que inicia no zero, então, nesse caso, o print seria "!"

# Int (números sem parte decimal)
print(1 + 2) #Os int diferenciam-se de uma string por não terem aspas duplas os envolvendo. É assim que o programa saberá se deve concatenar 2 textos ou somar 2 números
print(123_456) #Para expressar números grandes, ao invés de usar vírgula - padrão americano - ou ponto - padrão brasileiro - é possível usar underline, o programa irá ignorar esse caracter, porém fica mais fácil de identificar qual o número

# Float (números com parte decimal)
print(3.14159) #Lembrar que, devido ao padrão americano, deve-se usar . ao invés de , para dividir o valor decimal de um número

#Boolean (Verdadeiro ou Falso)
print(True)
print(False)