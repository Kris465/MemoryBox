def input_heights():
    data = input("Введите рост 22 учеников, разделённые пробелом: ")
    heights = [float(x) for x in data.strip().split()]
    if len(heights) != 22:
        print("Ошибка: необходимо ввести ровно 22 значения.")
        return None
    return heights


def main():
    heights = input_heights()
    if heights is None:
        return

    r = float(input("Введите значение r: "))

    count = sum(1 for h in heights if h <= r)

    print(f"Количество учеников с ростом не превышающим {r}: {count}")


if __name__ == "__main__":
    main()
