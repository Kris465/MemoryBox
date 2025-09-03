def which_come_first(n):
    return "Цифра 2 левее" if str(n).find('2') < str(n).find('5') else "Цифра 5 левее"

# Пример использования
n = 123452
print(which_come_first(n))
