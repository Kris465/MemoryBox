import turtle
import math

t = turtle.Turtle()
t.shape('turtle')

for x in range(-300, 300):
    y = 50 * math.sin(x / 20)
    t.goto(x, y)

turtle.exitonclick()
