import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")
screen.colormode(255)

t = turtle.Turtle()
t.speed(0)
t.width(2)


def random_color():
    return (random.randint(50, 200),
            random.randint(50, 200),
            random.randint(50, 200))


def broken_line(segments):
    t.penup()
    t.goto(random.randint(-300, 300), random.randint(-300, 300))
    t.pendown()
    t.color(random_color())
    for _ in range(segments):
        angle = random.randint(-60, 60)
        length = random.randint(20, 100)
        t.left(angle)
        t.forward(length)


for _ in range(30):
    broken_line(random.randint(3, 10))

t.width(1)
for _ in range(20):
    t.color(255, 255, 255, 0.3)
    broken_line(random.randint(2, 5))

t.hideturtle()
turtle.exitonclick()
