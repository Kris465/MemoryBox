import turtle
import math

screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Параметры глаза
eye_radius = 50
pupil_radius = 10
eye_center_y = -50  # Центр глаза по Y


# Рисуем глазное яблоко (белый круг)
def draw_eye():
    t.clear()
    t.penup()
    t.goto(0, eye_center_y - eye_radius)  # Начальная позиция для рисования круга
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    t.circle(eye_radius)
    t.end_fill()


# Ограничиваем движение зрачка внутри глаза
def follow_mouse(x, y):
    draw_eye()

    # Вычисляем вектор от центра глаза до курсора
    dx = x - 0
    dy = y - eye_center_y
    distance = math.sqrt(dx**2 + dy**2)

    # Если курсор за пределами глаза - нормализуем вектор
    if distance > (eye_radius - pupil_radius):
        scale = (eye_radius - pupil_radius) / distance
        dx *= scale
        dy *= scale

    # Позиция зрачка (центр зрачка)
    pupil_x = 0 + dx
    pupil_y = eye_center_y + dy

    t.penup()
    t.goto(pupil_x, pupil_y - pupil_radius)  # Позиция для рисования круга
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    t.circle(pupil_radius)
    t.end_fill()


# Рисуем глаз при запуске
draw_eye()

screen.onclick(follow_mouse)
turtle.done()
