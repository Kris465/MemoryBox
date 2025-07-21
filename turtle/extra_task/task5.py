import turtle
from random import randint, choice


t = turtle.Turtle()
t.shape('turtle')

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple',
          'pink', 'gold', 'cyan', 'magenta']

for i in range(10):
    x = randint(-300, 300)
    y = randint(-300, 300)

    color = choice(colors)
    size = randint(10, 30)

    t.penup()
    t.goto(x, y)
    t.pendown()
    t.dot(size, color)

turtle.exitonclick()
