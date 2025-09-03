import turtle

t = turtle.Turtle()
t.speed(0)
t.width(2)
t.color("lightcyan")
turtle.bgcolor('blue')


def fancy_branch(size, levels):
    if levels == 0:
        t.forward(size)
        return
    size /= 3.0
    fancy_branch(size, levels-1)
    t.left(60)
    fancy_branch(size, levels-1)
    t.right(120)
    fancy_branch(size, levels-1)
    t.left(60)
    fancy_branch(size, levels-1)


for _ in range(6):
    fancy_branch(150, 3)
    t.right(60)

turtle.exitonclick()
