enemies = 1

def increaseEnemies():
    enemies = 0      # Para o código não dar erro, é necessário definir localmente a variável enemies
    enemies += 2     # A verdade é que essa variável é totalmente diferente da global, elas só acabaram tendo o mesmo nome, então, enemies = 2 não altera de fato a variável global
    print(f"Inimigos dentro da função: {enemies}")
# Editar a variável local enemies, fará com que o código resulte em um erro, pois ele acha que estamos editando uma variável que não existe (não foi definida dentro da função), ao invés de estarmos tentando editar a variável global enemies

def increaseGlobalEnemies():
    # Para acessar e modificar a variável global, precisamos EXPLICITAR que a variável a ser acessada e modificada é global. No entanto, isso pode ser confuso, e geralmente acarreta em erros e bugs facilmente
    # É mais fácil e, principalmente, seguro, utilizar returns alterando a variável, ao invés de modificar uma variável global
    global enemies
    enemies += 1


increaseEnemies()
print(f"Inimigos fora da função: {enemies}")