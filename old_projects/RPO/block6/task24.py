x = int(input("Введите число x: "))

sum_greater_x = 0
even_count = 0

while True:
    number = int(input("Введите число: "))
    if number == 0:
        break
    
    if number > x:
        sum_greater_x += number
        
    if number % 2 == 0:
        even_count += 1
        
print(f"Сумма чисел больших x: {sum_greater_x}")
print(f"количество четных чисел {even_count}")
