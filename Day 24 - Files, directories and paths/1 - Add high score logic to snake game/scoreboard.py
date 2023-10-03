from turtle import Turtle


ALINHAMENTO = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.pontuacao = 0
        self.pontuacao_maxima = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()

    def atualizar_pontuacao(self):
        self.clear()
        self.write(
            f"Score: {self.pontuacao} High score: {self.pontuacao_maxima}",
            align=ALINHAMENTO,
            font=FONT
        )

    def aumentar_pontuacao(self):
        self.pontuacao += 1
        self.atualizar_pontuacao()

    # Para implementar o high score, é necessário abandonar a lógica do game over, e implementar
    # uma lógica de resetar o jogo.
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(
    #         "GAME OVER", align=ALINHAMENTO, font=FONT
    #     )

    def reset(self):
        # Se a pontuação do jogo atual for maior do que a maior pontuação já gravada, então esse
        # valor é atualizado.
        if self.pontuacao > self.pontuacao_maxima:
            self.pontuacao_maxima = self.pontuacao
        # Por fim, a pontuação é resetada para o próximo jogo.
        self.pontuacao = 0
