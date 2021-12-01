import random

nameList = ['Asafe', 'Aurea', 'Ju', 'Yuri', 'Vlad', 'Guta'] #Lista pronta

randomPerson = random.randint(0, (len(nameList)-1))

print(f"{nameList[randomPerson]} irá pagar a conta!")

# Lista recebendo inputs do usuário. O usuário digita os nomes separando por vírgula e a função split() é capaz de separar o input tirando o que foi passado no parâmetro da função. Exemplo: input = a, b, c, d. O python colocará isso na lista ['a', 'b', 'c', 'd'], pois foi retirado o ", " do input e separado "o que sobrou" em uma lista

nomesString = input("Quem vai sair pra jantar?")

nomes = nomesString.split(", ")

pagante = random.randint(0, (len(nomes)-1))

print(f"{nomes[pagante]} irá pagar a conta!")

# Vale ressaltar que ainda é possível fazer a escolha de uma pessoa pela função random.choice(), feita para listas, que irá levar em conta o offset dos índices e se ajustando ao tamanho da lista

pgt = random.choice(nameList)

print(f"{pgt} irá pagar a conta!")