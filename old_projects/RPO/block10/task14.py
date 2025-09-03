def is_power_of_five(n):
    if n < 1 or n & (n - 1) != 0:
        return False
    while n >= 5 and n % 5 == 0:
        n //= 5
    return n == 1


n = int(input("Введите чиссло: "))
sequence = list(map(int, input().split()))[:n]

result = sum(1 for number in sequence if is_power_of_five(number))

print(result)
