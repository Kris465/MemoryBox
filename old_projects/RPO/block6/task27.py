def analyze_digits(n):
    digits = str(n)
    min_d = min(digits)
    max_d = max(digits)
    return {
        'максимальная_цифра': int(max_d),
        'минимальная_цифра': int(min_d),
        'разница': int(max_d) - int(min_d),
        'сумма': int(max_d) + int(min_d)
    }
    
    
number = 12345
result = analyze_digits(number)
print(f"Анализ числа {number}: ")
for key, value in result.items():
    print(f"{key}: {value}")
