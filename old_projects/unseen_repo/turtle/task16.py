import turtle
import colorsys

t = turtle.Turtle()
t.speed(0)
turtle.colormode(255)
turtle.bgcolor('black')
t.width(2)

for i in range(200):
    hue = i / 200
    saturation = 1.0
    value = 1.0
    r, g, b = colorsys.hsv_to_rgb(hue, saturation, value)

    t.pencolor(int(r * 255), int(g * 255), int(b * 255))
    t.width(2 + (i % 10)/2)

    t.forward(200)
    t.backward(200)
    t.left(1)

t.penup()
t.goto(0, -20)
t.pendown()
t.fillcolor('gold')
t.begin_fill()
t.circle(20)
t.end_fill()

t.penup()
t.goto(0, -50)
t.pendown()
t.color('white')
t.write("Калейдоскоп", align="center", font=("Arial", 16, "bold"))

t.hideturtle()
turtle.exitonclick()
