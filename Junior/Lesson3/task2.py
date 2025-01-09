def sum_of_numbers():
    numbers = []
    while True:
        user_input = input("Введите число (или 'stop' для завершения): ")
        if user_input.lower() == 'stop':
            break
        numbers.append(int(user_input))

    print(f"Сумма введенных чисел: {sum(numbers)}")


sum_of_numbers()
