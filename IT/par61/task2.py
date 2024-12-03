# Гюнашян Владислав
import turtle

window = turtle.Screen()
window.title('Sierpinski')
window.bgcolor('lightblue')

alex = turtle.Turtle()


def sierpinski(a, t, size):
    if a == 0:
        for i in range(3):
            t.forward(size)
            t.left(120)
            
    else:
        sierpinski(a-1, t, size/2)
        t.forward(size/2)
        sierpinski(a-1, t, size/2)
        t.forward(size/2)
        t.left(120)
        t.forward(size/2)
        sierpinski(a-1, t, size/2)
        t.forward(size/2)
        t.left(120)
        t.forward(size)
        t.left(120)


sierpinski(3, alex, 200)

window.mainloop()

