n = int(input("Введите натуральное число: "))
a = int(input("Введите значение a (0 ≤ a ≤ 8): "))
x = int(input("Введите значение x: "))
y = int(input("Введите значение y: "))


def analyze_number(n, a, x, y):

    str_n = str(n)
    

    count_a = str_n.count(str(a))
    

    count_multiples = sum(1 for digit in str_n if int(digit) % x == 0)
    

    sum_greater_a = sum(int(digit) for digit in str_n if int(digit) > a)
    

    count_x = str_n.count(str(x))
    count_y = str_n.count(str(y))
    
    return count_a, count_multiples, sum_greater_a, count_x + count_y


results = analyze_number(n, a, x, y)
print(f"а) Цифра {a} встречается {results[0]} раз.")
print(f"б) Количество цифр, кратных {x}: {results[1]}.")
print(f"в) Сумма цифр, больших {a}: {results[2]}.")
print(f"г) Цифры {x} и {y} встречаются {results[3]} раз.")