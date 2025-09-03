import turtle


t = turtle.Turtle()
t.shape('turtle')
t.width(3)


def celtic_knot():
    for _ in range(4):
        t.forward(100)
        t.circle(30, 100)
        t.forward(100)
        t.left(90)


celtic_knot()
turtle.exitonclick()
