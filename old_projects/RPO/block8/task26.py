n = int(input("Введите значение n: "))


def count_divisors(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    return count


for number in range(1, n + 1):
    divisors_count = count_divisors(number)
    print(f"{number}: {'+' * divisors_count}")
