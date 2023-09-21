from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def mover(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # Outra maneira de tratar a colisão é fazendo o método de 'bounce', que só alteraria a
    # direção da bola, a verificação seria feita no laço while do main
    def quicar(self, direcao):
        if direcao == "y":
            self.y_move *= -1
            # A redução do atributo move_speed se dá pois quanto menor o tempo de sleep do método
            # time.sleep, mais rápida a tela atualiza, e mais rápido a bola se move
            self.move_speed *= 0.95
        elif direcao == "x":
            self.x_move *= -1
            self.move_speed *= 0.95

    def resetar_posicao(self):
        self.goto(0, 0)
        self.quicar(direcao="x")
        self.move_speed = 0.1
