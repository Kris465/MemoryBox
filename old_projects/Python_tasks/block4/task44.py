a = int(input('Введите a: '))
b = int(input('Введите b: '))
c = int(input('Введите c: '))
d = int(input('Введите d: '))

if a % b == c or a % b == d:
    print('Одно из чисел c, b равно остатку')
else:
    print('Неверно')
