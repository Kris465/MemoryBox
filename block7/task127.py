def is_prime_recursive(n, d=None):
    d = d or int(n ** 0.5)

    match(n < 2, d == 1, n % d == 0):
        case (True, _, _):
            return "Число не простое"
        case (_, True, _):
            return "Число простое"
        case (_, _, True):
            return "Число простое"


num = int(input("Введите число"))
print(is_prime_recursive(num))
