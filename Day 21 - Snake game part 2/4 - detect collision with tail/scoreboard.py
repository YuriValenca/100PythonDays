from turtle import Turtle


ALINHAMENTO = "center"
FONT = ("Courier", 24, "normal")


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
            f"Score: {self.pontuacao}", align=ALINHAMENTO, font=FONT
        )

    def aumentar_pontuacao(self):
        self.pontuacao += 1
        self.clear()
        self.atualizar_pontuacao()

    def game_over(self):
        self.goto(0, 0)
        self.write(
            "GAME OVER", align=ALINHAMENTO, font=FONT
        )
