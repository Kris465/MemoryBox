import turtle
import random


t = turtle.Turtle()
t.shape('turtle')
turtle.bgcolor('blue')


def draw_star(x, y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color('gold')
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()


for _ in range(20):
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    size = random.randint(10, 30)
    draw_star(x, y, size)

turtle.exitonclick()
