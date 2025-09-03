import turtle
import colorsys

t = turtle.Turtle()
turtle.colormode(255)
t.speed(0)
t.shape('turtle')
t.penup()
t.goto(-100, -100)
t.pendown()

size = 200

for y in range(size):
    for x in range(size):
        hue = x / size  # Горизонтальный градиент (можно заменить на (x + y) / (2 * size) для диагонального)
        r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
        t.pencolor(int(r * 255), int(g * 255), int(b * 255))
        t.forward(1)
    t.penup()
    t.goto(-100, -100 + y + 1)
    t.pendown()

turtle.exitonclick()
