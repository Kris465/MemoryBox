<<<<<<< HEAD
b = [8431, 1234, 326, 312, 75, 4345, 23, 10]
count = 0

for number in b:
    if number < 100:
        count += 1

print(f'Количество чисел меньше 100: {count}')
=======
count = 0
n = 1

while True:
    bn = n ** 3
    if bn >= 100:
        break
    count += 1
    n += 1

print(count)
>>>>>>> db601d430cb832b2128b1b19d7480eb6966c95df
