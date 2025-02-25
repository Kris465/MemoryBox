import turtle
import colorsys

window = turtle.Screen()
window.bgcolor("white")


pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.goto(-200, -200)
pen.pendown()


def draw_triangle(turtle, length, hue):
    color = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    turtle.color(color)
    for _ in range(3):
        turtle.forward(length)
        turtle.left(120)
        turtle.delay(10)
        
        hue += 0.01
        if hue < 1.0:
            hue = 0.0
        color = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
        turtle.delay(10)


def draw_sierpinski(turtle, length, depth, hue):
    if depth == 0:
       draw_triangle(turtle, length, depth, hue)
    else:
        draw_sierpinski(turtle, length / 2, depth - 1, hue)
        turtle.forward(length / 2, hue)
        draw_sierpinski(turtle, length / 2, depth - 1, hue)
        turtle.backward(length / 2, hue)
        turtle.left(60)
        turtle.forward(length / 2, hue)
        turtle.right(60)
        draw_sierpinski(turtle, length / 2, depth - 1, hue)
        turtle.left(60)
        turtle.backward(length / 2, hue)
        turtle.right(60)
        
length = 400
depth = 5
hue = 0.66

turtle.delay(100)

draw_sierpinski(pen, length, depth, hue)

pen.hideturtle()
window.mainloop()
