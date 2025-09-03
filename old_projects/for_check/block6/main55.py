def is_increasing(number):
    num_str = str(number)
    
    for i in range(len(num_str) - 1):
        if num_str[i] > num_str[i + 1]:
            return False
            
    return True

# Примеры использования
number1 = 1478
number2 = 1782
number3 = 1668

print(f"{number1}: {'Да' if is_increasing(number1) else 'Нет'}")
print(f"{number2}: {'Да' if is_increasing(number2) else 'Нет'}")
print(f"{number3}: {'Да' if is_increasing(number3) else 'Нет'}")
