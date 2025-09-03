import turtle
import math

def draw_ellipse(x, y, a, b, color):
    turtle.penup()
    turtle.goto(x, y + b)  # Начинаем с верхней точки эллипса
    turtle.pendown()
    turtle.color(color)
    
    for angle in range(0, 361, 2):  # Шаг 2° для более гладкой кривой
        rad = math.radians(angle)
        x_pos = x + a * math.sin(rad)  # Горизонтальное положение
        y_pos = y + b * math.cos(rad)  # Вертикальное положение
        turtle.goto(x_pos, y_pos)

# Настройки
turtle.Screen().bgcolor("white")
turtle.speed(0)  # Максимальная скорость
turtle.hideturtle()  # Скрываем черепашку

# Рисуем первый эллипс (синий)
draw_ellipse(0, 0, 30, 80, "blue")

# Рисуем второй эллипс (красный), накладывающийся на первый
draw_ellipse(0, 0, 50, 60, "red")

turtle.done()
