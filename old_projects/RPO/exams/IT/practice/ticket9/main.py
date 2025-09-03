import turtle

def draw_circle(color, radius):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

turtle.speed(0)
turtle.bgcolor("black")

for r in range(0, 256, 51):
    for g in range(0, 256, 51):
        for b in range(0, 256, 51):
            color = (r/255, g/255, b/255)
            draw_circle(color, 50)
            turtle.penup()
            turtle.forward(100)
            turtle.pendown()
        turtle.penup()
        turtle.goto(0, turtle.ycor() - 100)
        turtle.pendown()
        turtle.goto(0, 0)

turtle.hideturtle()
turtle.done()
