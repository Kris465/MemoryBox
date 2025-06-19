import turtle


t = turtle.Turtle()
t.shape('turtle')


for i in range(30):
    for _ in range(4):
        t.forward(10 + i * 5)
        t.left(90)
    t.left(15)

turtle.exitonclick()
