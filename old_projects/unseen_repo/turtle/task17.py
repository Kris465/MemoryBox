import turtle

# Настройка экрана
screen = turtle.Screen()
screen.bgcolor("white")

# Создаем черепашку для пикселей
pixel = turtle.Turtle()
pixel.speed(0)
pixel.hideturtle()
pixel.penup()

# Размер одного "пикселя"
PIXEL_SIZE = 20

# Пиксельная карта сердечка (1 - рисовать, 0 - пропустить)
heart_pixels = [
    [0, 1, 1, 0, 0, 0, 1, 1, 0],
    [1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0]
]


def draw_pixel_art(pixel_map, color):
    start_x = -len(pixel_map[0]) * PIXEL_SIZE / 2
    start_y = len(pixel_map) * PIXEL_SIZE / 2

    for y in range(len(pixel_map)):
        for x in range(len(pixel_map[0])):
            if pixel_map[y][x] == 1:
                pixel.goto(start_x + x * PIXEL_SIZE, start_y - y * PIXEL_SIZE)
                pixel.color(color)
                pixel.begin_fill()
                for _ in range(4):
                    pixel.forward(PIXEL_SIZE)
                    pixel.right(90)
                pixel.end_fill()


# Рисуем красное сердечко
draw_pixel_art(heart_pixels, "red")

# Подпись
pixel.goto(0, -150)
pixel.color("black")
pixel.write("Пиксельное сердце", align="center", font=("Arial", 16, "normal"))

turtle.exitonclick()
