# Mapa do tesouro

row1 = ["😃", "😃", "😃"]
row2 = ["😃", "😃", "😃"]
row3 = ["😃", "😃", "😃"]

map = [row1, row2, row3] # Essa lista configura uma lista aninhada, uma lista de listas

print(f"{row1}\n{row2}\n{row3}")

position = input("Onde vc deseja esconder o tesouro?")

horizontal = int(position[0]) # Primeiro caracter do input
vertical = int(position[1]) # Segundo caracter do input

selectedRow = map[horizontal-1]   # Selected row pega o elemento do 1o input -1 e seleciona uma das 3 listas
selectedRow[vertical - 1] = " X " # Em seguida, o 2o input -1 (nos dois casos, para evitar out of bounds) define qual dos 3 elementos será alterado por X

print(f"{row1}\n{row2}\n{row3}")