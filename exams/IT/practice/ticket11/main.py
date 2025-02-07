def to_boolean(value):
    if value.lower() == 'true':
        return True
    elif value.lower() == 'false':
        return False
    else:
        raise ValueError("Некорректное значение. Пожалуйста, введите True или False.")

def logical_operation(a, b, c, operation):
    if operation == 'or':
        return a or b or c
    elif operation == 'and':
        return a and b and c
    elif operation == 'xor':
        return a ^ b ^ c
    else:
        raise ValueError("Неправильный тип логической операции. Используйте 'and', 'or' или 'xor'.")

def print_truth_table(operation):
    print(f"\nТаблица истинности для операции '{operation}':")
    print(" A      B      C      Result")
    print("---------------------------------")
    for a in [False, True]:
        for b in [False, True]:
            for c in [False, True]:
                result = logical_operation(a, b, c, operation)
                print(f"{a:<7} {b:<7} {c:<7} {result}")

def main():
    try:
        a = to_boolean(input("Введите значение первого операнда (True/False): "))
        b = to_boolean(input("Введите значение второго операнда (True/False): "))
        c = to_boolean(input("Введите значение третьего операнда (True/False): "))
        operation = input("Введите тип логической операции (and, or, xor): ").strip().lower()

        result = logical_operation(a, b, c, operation)
        print(f"\nРезультат: {a} {operation} {b} {operation} {c} = {result}")

        print_truth_table(operation)

    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
