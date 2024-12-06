def draw_triangle(fill, base=10):
    n = 1
    for i in range(base):
        i = [fill] * n
        print(''.join(i))
        n += 1


draw_triangle('*')
