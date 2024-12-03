#Николаев Вадим
def sum_of_divisors(num):
    total = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            total += i
    return total


def amicable_numbers(limit):
    pairs = []
    for num in range(2, limit):
        partner = sum_of_divisors(num)
        if partner != num and sum_of_divisors(partner) == num:
            pairs.append((num, partner))
    return list(set(tuple(sorted(pairs))for pair in pairs))


limit = 10000
print("Пары дружественных чисел:", amicable_numbers(limit))