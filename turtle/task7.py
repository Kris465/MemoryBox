import turtle


t = turtle.Turtle()
t.width(3)
t.shape('turtle')

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(360):
    t.pencolor(colors[i % 6])
    t.forward(1)
    t.left(1)

turtle.exitonclick()
