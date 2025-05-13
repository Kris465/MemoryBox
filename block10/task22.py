def max_of_two(a, b):
    """
    Функция возвращает максимум из двух чисел.
    """
    return a if a > b else b


nums = [
    int(input("Введите первое число: ")),
    int(input("Введите второе число: ")),
    int(input("Введите третье число: ")),
    int(input("Введите четвертое число: ")),
    int(input("Введите пятое число: ")),
    int(input("Введите шестое число: "))
]


max_value = nums[0]
for num in nums[1:]:
    max_value = max_of_two(max_value, num)


print(f"Наибольшее число: {max_value}")
