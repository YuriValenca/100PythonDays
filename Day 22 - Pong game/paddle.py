from turtle import Turtle


class Paddle(Turtle):
    # Notar a criação da classe com um parâmetro a mais, pois a posição de cada paddle é diferente, mas eles são iguais
    def __init__(self, posicao):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(posicao)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def cima(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def baixo(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
