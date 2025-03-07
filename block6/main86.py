def which_come_righter(n, a, b):
    return f"Цифра {a} правее" if str(n).rfind(str(a)) > str(n).rfind(str(b)) else f"Цифра {b} правее"

# Пример использования
n = 123452
a = 2
b = 5
print(which_come_righter(n, a, b))
