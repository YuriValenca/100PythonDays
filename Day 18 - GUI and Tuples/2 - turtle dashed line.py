from turtle import Turtle, Screen

timmy = Turtle()
tela = Screen()

for i in range(15):
    timmy.forward(10)
    timmy.penup()
    # Avança 10 e "levanta" a caneta
    timmy.forward(10)
    timmy.pendown()
    # Avança 10 e "abaixa" a caneta

tela.exitonclick()
