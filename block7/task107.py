n = int(input("Введите натуральное число n: "))
numbers = []


for i in range(n):
    num = int(input(f"Введите исло a{i + 1}: "))
    numbers.append(num)

x = int(input("Введите число x: "))

count_negative = sum(1 for num in numbers if num < 0)

is_count_greather_than_x = count_negative > x

print(f"Количество отрицательных чисел превышает {x}: \
      {is_count_greather_than_x}")
