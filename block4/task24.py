x = int(input('Введите двухзначное число: '))

a = (x // 10) ** 3
b = (x % 10) ** 3
c = x ** 2
d = (a + b) * 4

if c == d:
    print('True')
else:
    print('False')
