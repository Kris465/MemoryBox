from random import randint

def get_user_input():
    while True:
        try:
            a = int(input('Введите начало диапазона: '))
            b = int(input('Введите конец диапазона: '))
            c = int(input('Введите размер списка: '))
            if a >= b:
                print("Ошибка: Начало диапазона должно быть меньше конца.")
                continue
            if c <= 0:
                print("Ошибка: Размер списка должен быть положительным.")
                continue
            return a, b, c
        except ValueError:
            print("Ошибка: Пожалуйста, введите корректные целые числа.")

def generate_random_list(a, b, c):
    return [randint(a, b) for _ in range(c)]

def create_node(value):
    return {'value': value, 'left': None, 'right': None}

def insert(root, value):
    if root is None:
        return create_node(value)
    if value < root['value']:
        root['left'] = insert(root['left'], value)
    else:
        root['right'] = insert(root['right'], value)
    return root

def order(node, sorted_values):
    if node is not None:
        order(node['left'], sorted_values)
        sorted_values.append(node['value'])
        order(node['right'], sorted_values)

def main():
    a, b, c = get_user_input()
    random_list = generate_random_list(a, b, c)
    root = None
    for value in random_list:
        root = insert(root, value)

    sorted_values = []
    order(root, sorted_values)

    print('Изначальный массив:', random_list)
    print('Отсортированный массив:', sorted_values)


if __name__ == "__main__":
    main()
