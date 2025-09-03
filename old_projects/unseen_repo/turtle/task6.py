import turtle

t = turtle.Turtle()
t.speed(0)
t.color("cyan")
turtle.bgcolor("blue")


def draw_branch(size):
    if size < 10:
        return
    else:
        for angle in [45, -90, 45, 0]:
            t.forward(size)
            draw_branch(size/3)
            t.backward(size)
            t.left(angle)


for _ in range(6):
    draw_branch(50)
    t.right(60)

turtle.exitonclick()
