import turtle


t = turtle.Turtle()
t.shape('turtle')
turtle.bgcolor("blue")


def hexagon(size, color):
    t.color(color)
    t.begin_fill()
    for _ in range(6):
        t.forward(size)
        t.left(60)
    t.end_fill()


colors = ["#FFD700", "#FFEC88", "#EEE8AA"]

for row in range(5):
    for col in range(5):
        x = col * 60
        y = row * 50
        if row % 2 == 1:
            x += 30

        t.penup()
        t.goto(x, y)
        t.pendown()
        hexagon(30, colors[(row+col) % 3])

turtle.exitonclick()
