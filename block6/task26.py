def find_max_min_digits(n):
    digits = str(n)
    
    max_digit = max(int(d) for d in digits)
    
    min_digit = min(int(d) for d in digits)
    
    return {
        'максимальная_цифра' : max_digit,
        'минимальная_цифра' : min_digit
    }
    
    
examples = [
    12345,
    999,
    1000,
    54321,
    112233
]

for number in examples: 

    result = find_max_min_digits(number)
    print(f"число: {number}")
    print(f"Результаты: ")
    for key, value in result.items():
        print(f"   {key}: {value}")
    print()
