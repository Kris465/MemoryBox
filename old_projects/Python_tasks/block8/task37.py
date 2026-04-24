def sum_of_divisors(n):
    total = 0
    for i in range(1, n + 1):
        if n % i == 0:
            total += i
    return total


a = int(input("Введите значение a: "))
b = int(input("Введите значение b: "))

max_sum = 0
number_with_max_sum = a

for number in range(a, b + 1):
    current_sum = sum_of_divisors(number)
    if current_sum > max_sum:
        max_sum = current_sum
        number_with_max_sum = number

print(f"Число с максимальной суммой делителей в интервале от {a} до {b}:\
    {number_with_max_sum} (Сумма делителей: {max_sum})")
