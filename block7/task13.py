def get_divisors(n):
    """Возвращает отсортированный  список всех делителей натурального
    числа n."""
    divisors = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return sorted(divisors)


def task_a(n):
    return get_divisors(n)


def task_b(n):
    return sum(get_divisors(n))


def task_c(n):
    return sum(x for x in get_divisors(n) if x % 2 != 0)


def task_d(n):
    return len(get_divisors(n))


def task_e(n):
    return len([x for x in get_divisors(n) if x % 2 != 0])


def task_f(n):
    divisors = get_divisors(n)
    total = len(divisors)
    even = len([x for x in divisors if x % 2 == 0])
    return total, even


def task_g(n, d):
    return len([x for x in get_divisors(n) if x > d])


n = 6
print("a) Делители:", task_a(n))
print("б) Сумма делителей:", task_b(n))
print("в) Сумма четных делителей: ", task_c(n))
print("г) Количество делителей: ", task_d(n))
print("д) Нечетных делителей: ", task_e(n))
print("е) Всего и четных: ", task_f(n))
print("ж) Делителей > 3: ", task_g(n, 3))
