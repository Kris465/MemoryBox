def find_leftmost_digit(number, a, b):
    number_str = str(number)

    pos_a = number_str.find('2')
    pos_b = number_str.find('5')

    if pos_a == -1 and pos_b == -1:
        return f"Цифры {a} и {b} отсутсвуют в числе"
    elif pos_a == -1:
        return f"В числе отсутсвует число {b} и есть число {a}"
    elif pos_b == -1:
        return f"В числе отсутсвует число {a} и есть число {b}"
    elif pos_a < pos_b:
        return f"Цифра {b} расположена левее чем {a}"
    else:
        return f"Цифра {a} расположена левее чем {b}"


num = int(input("Введите число: "))
a = int(input("Введите первую цифру для поиска: "))
b = int(input("Введите вторую цифру для поиска: "))

print(find_leftmost_digit(num, a, b))
