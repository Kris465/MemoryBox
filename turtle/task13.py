import turtle
import math

t = turtle.Turtle()
t.speed(0)
t.width(2)

RAY_COUNT = 5
WEB_RADIUS = 200
CENTER_X, CENTER_Y = 0, -50

t.penup()
t.goto(CENTER_X, CENTER_Y)
t.pendown()
t.color("black")

for i in range(RAY_COUNT):
    angle = i * (360 / RAY_COUNT)
    rad = math.radians(angle)
    x = CENTER_X + WEB_RADIUS * math.sin(rad)
    y = CENTER_Y + WEB_RADIUS * math.cos(rad)
    t.goto(CENTER_X, CENTER_Y)
    t.goto(x, y)

t.color("gray")
for ring in [0.3, 0.6, 0.9]:
    points = []
    for i in range(RAY_COUNT):
        angle = i * (360 / RAY_COUNT)
        rad = math.radians(angle)
        x = CENTER_X + WEB_RADIUS * ring * math.sin(rad)
        y = CENTER_Y + WEB_RADIUS * ring * math.cos(rad)
        points.append((x, y))

    t.penup()
    t.goto(points[-1])
    t.pendown()
    for point in points:
        t.goto(point)

t.hideturtle()
turtle.exitonclick()
