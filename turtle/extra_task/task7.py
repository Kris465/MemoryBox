import turtle
from random import randint


t1 = turtle.Turtle()
t1.shape('turtle')
t1.color('red')
t1.penup()
t1.goto(-250, 30)

t2 = turtle.Turtle()
t2.shape('turtle')
t2.color('blue')
t2.penup()
t2.goto(-250, -30)

while t1.xcor() < 250 and t2.xcor() < 250:
    t1.forward(randint(1, 7))
    t2.forward(randint(1, 7))

winner = "Красная" if t1.xcor() > t2.xcor() else "Синяя"
t1.write(f"Победила {winner} черепаха!", font=('Arial', 14))

turtle.exitonclick()
