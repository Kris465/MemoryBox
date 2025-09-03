import turtle
'''
Создайте функцию рисования звезды. В то же время пользователь должен вводить длину стороны.
'''
turtle.shape("turtle")
turtle.pensize(8)
turtle.color('black')

def star():
    pass
    for i in range(10):
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.left(36)
    turtle.penup()
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.color('black')
    turtle.pendown()
    turtle.pensize(15)

star()
