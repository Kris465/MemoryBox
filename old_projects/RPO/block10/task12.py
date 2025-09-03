def is_even(number):
    return number % 2 == 0


a = []
print("Введите 8 целых чисел для первой последовательности:")
for i in range(8):
    a.append(int(input(f"a{i+1}: ")))

b = []
print("Введите 8 целых чисел для второй последовательности:")
for i in range(8):
    b.append(int(input(f"b{i+1}: ")))

count_even_a = sum(1 for num in a if is_even(num))
count_odd_b = sum(1 for num in b if not is_even(num))

print(f"Количество четных чисел в первой последовательности: {count_even_a}")
print(f"Количество нечетных чисел во второй последовательности: {count_odd_b}")
