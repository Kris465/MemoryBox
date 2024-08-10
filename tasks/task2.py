user_string = input('Введите последовательность чисел: ')
user_list = user_string.split()
number = input('Введите порядковый номкр числа: ')

print(user_list[int(number) - 1])
