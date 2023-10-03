from turtle import Turtle


ALINHAMENTO = "center"
FONT = ("Courier", 24, "normal")
# Uma solução para evitar colocar o path "cru" todas as vezes é utilizar uma string crua, passando
# o caminho relativo do arquivo de texto. Isso é feito colocando um 'r' antes da string, como no
# exemplo abaixo. Para obter o caminho relativo, basta clicar com o botão direito no arquivo, nesse
# caso, score.txt, e clicar em 'Copy Relative Path'.
FILE_PATH = r"Day 24 - Files, directories and paths\3 - Read and write a high score in the snake game\score.txt"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.pontuacao = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        # A mundaça ocorre também no atributo pontuacao_maxima, que agora irá ler o arquivo de
        # texto (convertendo o valor para inteiro), e esse valor será atribuído a pontuacao_maxima.
        with open(FILE_PATH) as file:
            self.pontuacao_maxima = int(file.read())

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

    def reset(self):
        if self.pontuacao > self.pontuacao_maxima:
            self.pontuacao_maxima = self.pontuacao
            # Essa linha de código será responsável por escrever no texto a nova pontuação,
            # caso ela seja maior que a pontuação máxima anterior.
            with open(FILE_PATH, mode="w") as file:
                file.write(f"{self.pontuacao_maxima}")
        self.pontuacao = 0
