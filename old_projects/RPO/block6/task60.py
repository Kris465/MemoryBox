numbers = list(map(int, input("Введите 20 чисел через пробел: ").split()))
found = True
for i, num in enumerate(numbers):
    if num % 10 == 7:
        print(f"число заканчивающиеся на 7 находится на позиции {i + 1}")
        found = True
        break

if not found:
    print("Числа заканчивающего на 7 нет")
