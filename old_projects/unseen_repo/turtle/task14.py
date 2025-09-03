import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

WIDTH = screen.window_width() // 2 - 20
HEIGHT = screen.window_height() // 2 - 20

balls = []
colors = ["red", "green", "blue", "yellow", "purple", "orange"]

for _ in range(6):
    ball = turtle.Turtle()
    ball.shape("circle")
    ball.shapesize(1.2)
    ball.color(random.choice(colors))
    ball.penup()

    ball.goto(
        random.randint(-WIDTH + 30, WIDTH - 30),
        random.randint(-HEIGHT + 30, HEIGHT - 30)
    )

    ball.dx = random.uniform(2, 5) * random.choice([-1, 1])
    ball.dy = random.uniform(2, 5) * random.choice([-1, 1])
    balls.append(ball)


def move_balls():
    for ball in balls:
        x, y = ball.xcor(), ball.ycor()
        if x > WIDTH or x < -WIDTH:
            ball.dx *= -1
            ball.goto(
                WIDTH - 1 if x > 0 else -WIDTH + 1,
                y
            )

        if y > HEIGHT or y < -HEIGHT:
            ball.dy *= -1
            ball.goto(
                x,
                HEIGHT - 1 if y > 0 else -HEIGHT + 1
            )

        ball.goto(x + ball.dx, y + ball.dy)

    screen.update()
    screen.ontimer(move_balls, 30)


move_balls()
turtle.exitonclick()
