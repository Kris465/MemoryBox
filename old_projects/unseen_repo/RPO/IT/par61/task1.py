import turtle


def draw_triangle(points, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.goto(points[0])
    turtle.goto(points[1])
    turtle.goto(points[2])
    turtle.goto(points[0])
    turtle.end_fill()


def sierpinski(points, depth):
    if depth == 0:
        draw_triangle(points, "black")
    else:
        mid01 = ((points[0][0] + points[1][0]) / 2, (points[0][1] + points[1][1]) / 2)
        mid12 = ((points[1][0] + points[2][0]) / 2, (points[1][1] + points[2][1]) / 2)
        mid20 = ((points[2][0] + points[0][0]) / 2, (points[2][1] + points[0][1]) / 2)

        sierpinski([points[0], mid01, mid20], depth - 1)
        sierpinski([points[1], mid01, mid12], depth - 1)
        sierpinski([points[2], mid12, mid20], depth - 1)


def main():
    turtle.speed(0)
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(-200, -150)
    turtle.pendown()

    points = [(-200, -150), (0, 200), (200, -150)]
    depth = 6  # уровень рекурсии
    sierpinski(points, depth)

    turtle.done()


main()
