import turtle
import colorsys

window = turtle.Screen()
window.bgcolor("white")


pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.goto(-200, -200)
pen.pendown()


def draw_triangle(turtle, length, diff):
    color = colorsys.hsv_to_rgb(diff, 1.0, 1.0)
    turtle.color(color)
    for _ in range(3):
        turtle.forward(length)
        turtle.left(120)


def draw_sierpinski(turtle, length, depth, diff):
    if depth == 0:
        draw_triangle(turtle, length, diff)
    else:
        draw_sierpinski(turtle, length / 2, depth - 1, diff)
        turtle.forward(length / 2)
        draw_sierpinski(turtle, length / 2, depth - 1, diff + 0.2)
        turtle.backward(length / 2)
        turtle.left(60)
        turtle.forward(length / 2)
        turtle.right(60)
        draw_sierpinski(turtle, length / 2, depth - 1, diff + 0.4)
        turtle.left(60)
        turtle.backward(length / 2)
        turtle.right(60)


length = 400
depth = 5
dif = 0.66


draw_sierpinski(pen, length, depth, dif)

pen.hideturtle()
window.mainloop()
