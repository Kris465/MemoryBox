import turtle

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

SCALE = 30  # Размер чешуи
ROWS = 10   # Количество рядов
COLS = 15   # Количество столбцов


def draw_scale(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.setheading(-60)
    t.circle(SCALE, 120)
    t.end_fill()


for row in range(ROWS):
    for col in range(COLS):
        x_offset = SCALE * 0.8 if row % 2 else 0
        x = col * SCALE * 1.6 - (COLS*SCALE*0.8) + x_offset
        y = row * SCALE * 0.9 - (ROWS*SCALE*0.45)

        draw_scale(x, y)

turtle.exitonclick()
