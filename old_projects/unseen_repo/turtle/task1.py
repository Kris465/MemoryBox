import turtle


t = turtle.Turtle()
t.shape('turtle')


def nested_squares(size, steps):
    for i in range(steps):
        for _ in range(4):
            t.forward(size)
            t.left(90)
        size -= 20
        t.penup()
        t.goto(t.xcor() + 10, t.ycor() + 10)
        t.pendown()


nested_squares(200, 8)
turtle.exitonclick()
