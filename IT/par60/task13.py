# Фетисов Тимур
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_hiperprime(n):
    str_n = str(n)
    for i in range(len(str_n)):
        for j in range(i+1, len(str_n) + 1):
            if not is_prime(int(str_n[i:j])):
                return False
    return True


print(is_hiperprime(input('Введите число')))
