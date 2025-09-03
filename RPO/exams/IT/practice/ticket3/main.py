def convert_units(value, from_unit, to_unit):
    units = {
        'байт': 1,
        'килобайт': 1024,
        'мегабайт': 1024 ** 2,
        'гигабайт': 1024 ** 3
    }

    if from_unit in units and to_unit in units:
        byte_value = value * units[from_unit]
        converted_value = byte_value / units[to_unit]
        return int(converted_value)
    else:
        return None

def main():
    try:
        value = int(input("Введите количество: "))
        from_unit = input("Введите первую единицу измерения (байт, килобайт, мегабайт, гигабайт): ").strip()
        to_unit = input("Введите вторую единицу измерения (байт, килобайт, мегабайт, гигабайт): ").strip()

        result = convert_units(value, from_unit, to_unit)

        if result is not None:
            print(f'{value} {from_unit} = {result} {to_unit}')
        else:
            print("Ошибка: неверные единицы измерения.")
    except ValueError:
        print("Ошибка: введите корректное число.")


if __name__ == "__main__":
    main()
