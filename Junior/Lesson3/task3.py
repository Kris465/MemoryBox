def calculator():
    while True:
        num1 = float(input("Введите первое число: "))
        operation = input("Введите операцию (+, -, *, /) или 'exit' для выхода: ")
        if operation == 'exit':
            break
        num2 = float(input("Введите второе число: "))
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            result = num1 / num2 if num2 != 0 else "Ошибка: деление на ноль"
        else:
            result = "Неизвестная операция"
        
        print(f"Результат: {result}")

calculator()
