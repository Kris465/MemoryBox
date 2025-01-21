a = int(input("Введите сторону стола a: "))
b = int(input("Введите сторону стола b: "))
c = int(input("Введите сторону кости c: "))
d = int(input("Введите сторону кости d: "))
e = int(input("Введите сторону кости e: "))


def max_dominoes(a, b, c, d, e):
    if c > d:
        c, d = d, e
    if d > e:
        d, e = e, d
    if c > d:
        c, d = d, c

    max_count = 0
    if (c <= a and d <= b):
        max_count = (a // c) * (b // d)
    if (d <= a and c <= b):
        max_count = max(max_count, (a // d) * (b // c))
    if (d <= a and c <= b):
        max_count = max(max_count, (a // c) * (b // e))
    if (d <= a and c <= b):
        max_count = max(max_count, (a // e) * (b // c))
    if (d <= a and c <= b):
        max_count = max(max_count, (a // d) * (b // e))
    if (d <= a and c <= b):
        max_count = max(max_count, (a // e) * (b // d))

    return max_count


result = max_dominoes(a, b, c, d, e)
print(f'Макс колво костей домино которое можно разместить {result}')
