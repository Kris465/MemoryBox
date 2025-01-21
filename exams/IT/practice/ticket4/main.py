from random import randint

a = int(input('Введите начала диапозона: '))
b = int(input('Введите конец диапозона: '))
c = int(input('Введите размер списка: '))

chmo = []


for i in range(c):
    chmo.append(randint(a, b))


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


root = None
for value in chmo:
    root = insert(root, value)

sorted_values = []
order(root, sorted_values)


print('Изначальный массив:', chmo)
print('Отсортированый массив:', sorted_values)
