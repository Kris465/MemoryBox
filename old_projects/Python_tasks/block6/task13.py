def sequence(limit):
    a = 1
    result = []
    while a < limit:
        result.append(a)
        a += 1 / (len(result) + 1)  # Напоминает 1 + 1/2 + 1/3 + ...
    return result

# Пример использования
print(sequence(1.5))
