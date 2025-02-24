import math

def find_first_smaller(a):
    if not (1 < a < 1.5):
        raise ValueError("Число 'a' должно быть в интервале от 1 до 1.5")
    
    n = math.ceil(1 / a)
    
    return f"{1}/{n}"

a = 1.25
result = find_first_smaller(a)
print(f"Первое число, меньшее {a}: {result}")