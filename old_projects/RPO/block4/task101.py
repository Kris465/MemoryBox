def find_middle_number(a, b, c):
    if a < b < c or c < b < a:
        return b
    elif a < c < b or b < c < a:
        return c
    else:
        return a


a1, b1, c1 = map(float, input("Введите первую тройку чисел через пробел:")
                 .split())
a2, b2, c2 = map(float, input("Введите первую тройку чисел через пробел:")
                 .split())


middle_1 = find_middle_number(a1, b1, c1)
middle_2 = find_middle_number(a2, b2, c2)


average_of_middles = (middle_1 + middle_2) / 2

print(f'среднее фрифметическое средних чисел: {average_of_middles}')
