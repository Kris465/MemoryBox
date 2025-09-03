import turtle


t = turtle.Turtle()
t.shape('turtle')

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

for i in range(360):
    t.pencolor(colors[i % len(colors)])
    t.forward(2)
    t.left(1)

turtle.exitonclick()
