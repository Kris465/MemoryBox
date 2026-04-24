def get_month_number(n):
    if not isinstance(n, int):
        raise TypeError("Аргумент должен быть целым числом.")
    if 0 <= n <= 11:
        return n + 1
    else:
        raise ValueError("Номер месяца должен быть от 0 до 11.")


def main():
    while True:
        try:
            n = int(input("Введите номер месяца (от 0 до 11): "))
            month_number = get_month_number(n)
            print(f"Месяц: {month_number}")
            break
        except ValueError as e:
            print(e)
        except TypeError as e:
            print(e)


if __name__ == "__main__":
    main()
