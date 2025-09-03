import turtle

t = turtle.Turtle()
t.shape('turtle')
t.left(90)


def tree(size, angle=30):
    if size < 10:
        return
    t.forward(size)
    t.left(angle)
    tree(size * 0.7)
    t.right(angle * 2)
    tree(size * 0.7)
    t.left(angle)
    t.backward(size)


tree(100)
turtle.done()
