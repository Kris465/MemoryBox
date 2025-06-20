import turtle
import math


screen = turtle.Screen()
screen.bgcolor("black")

# Создаем Солнце
sun = turtle.Turtle()
sun.shape("circle")
sun.shapesize(2)
sun.color("yellow")

# Параметры планет (радиус орбиты, размер, цвет, скорость)
planets = [
    {"radius": 80,  "size": 0.5, "color": "gray",    "speed": 5},
    {"radius": 120, "size": 0.7, "color": "orange",  "speed": 3},
    {"radius": 180, "size": 0.8, "color": "blue",    "speed": 2},
    {"radius": 240, "size": 0.6, "color": "red",     "speed": 1}
]

# Создаем планеты
for p in planets:
    p["turtle"] = turtle.Turtle()
    p["turtle"].shape("circle")
    p["turtle"].shapesize(p["size"])
    p["turtle"].color(p["color"])
    p["turtle"].penup()
    p["angle"] = 0

# Анимация вращения
while True:
    for p in planets:
        p["angle"] += 0.01 * p["speed"]
        x = p["radius"] * math.cos(p["angle"])
        y = p["radius"] * math.sin(p["angle"])
        p["turtle"].goto(x, y)

    screen.update()
