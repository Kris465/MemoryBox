def swap(x, y):
    temp = x
    x = y
    y = temp
    return x, y


a = int(input('Введите a: '))
b = int(input('Введите b: '))
c = int(input('Введите c: '))
d = int(input('Введите d: '))

a, b = swap(a, b)

c, d = swap(c, d)

print(f'Новые значения:\n'
      f'a = {a}\n'
      f'b = {b}\n'
      f'c = {c}\n'
      f'd = {d}')
