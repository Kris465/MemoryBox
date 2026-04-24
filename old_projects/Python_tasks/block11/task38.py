# Исходный массив натуральных чисел
array = [7, 45, 123, 9, 56, 789, 1000, 88, 234]

# а) Все двузначные числа
print("Двухзначные числа:")
for element in array:
    if 10 <= element <= 99:
        print(element)

# б) Все трехзначные числа
print("\nТрехзначные числа:")
for element in array:
    if 100 <= element <= 999:
        print(element)
