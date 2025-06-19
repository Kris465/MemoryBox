import turtle

t = turtle.Turtle()
t.speed(0)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(36):
    t.color(colors[i % 6])
    t.circle(100)
    t.left(10)

turtle.exitonclick()
