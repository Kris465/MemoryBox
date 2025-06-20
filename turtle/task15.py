import turtle
import random

screen = turtle.Screen()
screen.bgcolor('midnightblue')
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.penup()
t.goto(-400, -200)
t.pendown()
t.color('black', 'dimgray')
t.begin_fill()
t.goto(400, -200)
t.goto(400, -250)
t.goto(-400, -250)
t.goto(-400, -200)
t.end_fill()

for x in range(-350, 350, 70):
    height = random.randint(100, 300)
    width = random.randint(40, 60)
    t.penup()
    t.goto(x, -200)
    t.pendown()
    t.color('black', 'gray')
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()
    t.color('yellow')
    for y in range(-180, -200 + height, 30):
        for x_window in range(x + 10, x + width - 10, 20):
            if random.random() > 0.3:
                t.penup()
                t.goto(x_window, y)
                t.pendown()
                t.begin_fill()
                for _ in range(4):
                    t.forward(10)
                    t.left(90)
                t.end_fill()

turtle.exitonclick()
