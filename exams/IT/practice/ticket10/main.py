def to_boolean(value):
    if value.lower() == 'true':
        return True
    elif value.lower() == 'false':
        return False
    else:
        raise ValueError("Некорректное значение. Пожалуйста, введите True или False.")


def main():
    try:
        first_operand = input("Введите первое логическое значение (True/False): ")
        second_operand = input("Введите второе логическое значение (True/False): ")

        first_operand = to_boolean(first_operand)
        second_operand = to_boolean(second_operand)

        and_result = first_operand and second_operand
        or_result = first_operand or second_operand
        not_first_result = not first_operand
        not_second_result = not second_operand

        print(f"Результат AND: {and_result}")
        print(f"Результат OR: {or_result}")
        print(f"Результат NOT первого операнда: {not_first_result}")
        print(f"Результат NOT второго операнда: {not_second_result}")

    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
