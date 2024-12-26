def calculate_expression(a):
    return 2 * a['x'] + 4 * a['y']


def check_condition_or(x, y):
    return (x == 0) or (y ** 2 == 4)


def check_condition_and(x, y):
    return (x == 0) and (y ** 2 == 4)


def check_multiplication_and_greater_than(x, y):
    return (x * y == 0) and (y > x)


def check_multiplication_or_less_than(x, y):
    return (x * y == 0) or (y < x)


def check_not_multiplication_and_greater_than(x, y):
    return (not (x * y < 0)) and (y > x)


def check_not_multiplication_or_greater_than(x, y):
    return (not (x * y < 0)) or (y > x)


data = [
    {'x': 1, 'y': 1},  # Для пункта а)
    {'x': 1, 'y': 2},  # Для пунктов б) и в)
    {'x': 2, 'y': 1},  # Для пунктов г), д) и е)
    {'x': 1, 'y': 2}   # Для пункта ж)
]
# Вычисления
results = []
for i, d in enumerate(data):
    if i == 0:
        results.append(calculate_expression(d))
    elif i == 1:
        results.append(check_condition_or(d['x'], d['y']))
        results.append(check_condition_and(d['x'], d['y']))
    elif i == 2:
        results.append(check_multiplication_and_greater_than(d['x'], d['y']))
        results.append(check_multiplication_or_less_than(d['x'], d['y']))
        results.append(
            check_not_multiplication_and_greater_than(d['x'], d['y']))
    else:
        results.append(
            check_not_multiplication_or_greater_than(d['x'], d['y']))

print("а):", results[0])
print("б):", results[1])
print("в):", results[2])
print("г):", results[3])
print("д):", results[4])
print("е):", results[5])
print("ж):", results[6])
