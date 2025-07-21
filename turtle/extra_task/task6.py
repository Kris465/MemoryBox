import turtle


t = turtle.Turtle()
t.shape('turtle')

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink']
size = 5
angle = 10

for i in range(100):
    t.color(colors[i % len(colors)])

    for j in range(4):
        t.forward(size)
        t.left(90)

    size += 2
    turtle.left(angle)


turtle.exitonclick()
