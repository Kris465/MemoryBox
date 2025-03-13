b = [8431, 1234, 326, 312, 75, 4345, 23, 10]
count = 0

for number in b:
    if number < 100:
        count += 1

print(f'Количество чисел меньше 100: {count}')
