import turtle as t
from random import randint


target = t.Turtle()
target.shape('circle')
target.color('red')
target.penup()

score = 0


def catch(x, y):
    global score
    if target.distance(x, y) < 20:
        score += 1
        t.title(f"счет: {score}")
        target.goto(randint(-200, 200), randint(-200, 200))


t.onscreenclick(catch)
catch(0, 0)
t.mainloop()
