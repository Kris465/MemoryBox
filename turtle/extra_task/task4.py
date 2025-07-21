import turtle


t = turtle.Turtle()
t.shape('turtle')
turtle.bgcolor("blue")
t.fillcolor("yellow")
t.pencolor("yellow")

t.begin_fill()

for i in range(5):
    t.forward(200)
    t.right(144)

t.end_fill()
turtle.exitonclick()
