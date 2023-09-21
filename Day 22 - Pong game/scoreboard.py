from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.pontuacao_esq = 0
        self.pontuacao_dir = 0

    def atualizar_pontuacao(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.pontuacao_esq, align="center",
                   font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.pontuacao_dir, align="center",
                   font=("Courier", 80, "normal"))

    def esq_ponto(self):
        self.pontuacao_esq += 1
        self.atualizar_pontuacao()

    def dir_ponto(self):
        self.pontuacao_dir += 1
        self.atualizar_pontuacao()
