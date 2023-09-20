from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.pontuacao = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()

    def atualizar_pontuacao(self):
        self.write(
            f"Score: {self.pontuacao}", align="center", font=("Arial", 14, "bold")
        )

    def aumentar_pontuacao(self):
        self.pontuacao += 1
        self.clear()
        self.atualizar_pontuacao()
