import turtle


t = turtle.Turtle()
t.shape('turtle')


def maze_pattern():
    for i in range(50):
        t.forward(5 + i * 2)
        t.left(90)


maze_pattern()
turtle.exitonclick()
