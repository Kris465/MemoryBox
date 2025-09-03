import turtle


t = turtle.Turtle()
t.shape('turtle')
t.color('red')

t.begin_fill()
t.left(90)
t.circle(100, 180)
t.left(180)
t.circle(100, 180)
t.left(40)
t.forward(300)

t.end_fill()

turtle.exitonclick()
