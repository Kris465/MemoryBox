def reverse_number(n):
    return int(str(n)[::-1])

def add_twos(n):
    return int('2' + str(n) + '2')

def remove_digit(n, a):
    return int(str(n).replace(str(a), ''))

def swap_first_last(n):
    s = str(n)
    if len(s) == 1:
        return n
    return int(s[-1] + s[1:-1] + s[0])

def duplicate_number(n):
    return int(str(n) * 2)

# Пример использования
n = 12345
a = 2

print("Исходное число:", n)
print("а) Реверсированное число:", reverse_number(n))
print("б) Число с добавлением двоек:", add_twos(n))
print("в) Число после удаления цифры", a, ":", remove_digit(n, a))
print("г) Число после перестановки первой и последней цифр:", swap_first_last(n))
print("д) Число после дублирования:", duplicate_number(n))
