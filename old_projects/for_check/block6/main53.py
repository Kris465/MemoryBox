def is_increasing_reverse(num):
    # Преобразуем число в строку и переворачиваем
    reversed_digits = str(num)[::-1]
    
    # Проверяем упорядоченность
    for i in range(len(reversed_digits) - 1):
        if reversed_digits[i] > reversed_digits[i + 1]:
            return False
    return True

# Примеры использования
numbers = [5321, 7820, 9663]

for number in numbers:
    result = is_increasing_reverse(number)
    print(f"Для числа {number} ответ: {'положительный' if result else 'отрицательный'}")
