def determine_type(value):
    if value.lower() in ['true', 'false']:
        return f"Тип: {type(value.lower() == 'true').__name__} (логическое значение)"

    try:
        int_value = int(value)
        return f"Тип: {type(int_value).__name__} (целое число)"
    except ValueError:
        pass

    try:
        float_value = float(value)
        if '.' in value or 'e' in value.lower():
            return f"Тип: {type(float_value).__name__} (число с плавающей запятой)"
    except ValueError:
        pass

    if value.startswith("[") and value.endswith("]"):
        try:
            list_value = eval(value)
            if isinstance(list_value, list):
                return f"Тип: {type(list_value).__name__} (список)"
        except Exception:
            pass

    if value.startswith("(") and value.endswith(")"):
        try:
            tuple_value = eval(value)
            if isinstance(tuple_value, tuple):
                return f"Тип: {type(tuple_value).__name__} (кортеж)"
        except Exception:
            pass
    return f"Тип: {type(value).__name__} (строка)"

def main():
    user_input = input("Введите что-то: ")
    result = determine_type(user_input)
    print(result)


if __name__ == "__main__":
    main()
