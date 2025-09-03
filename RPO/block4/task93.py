def classify_point(x, y, c):
    if (x <= 0 and y >= 0) or (x > 0 and y >= 0):
        return "1"
    elif (x <= 0 and y <= 0) or (x > 0 and y > 0):
        return "2"
    else:
        return "3"


def main():
    x = float(input("Введите координату X: "))
    y = float(input("Введите координату Y: "))
    c = float(input("Введите координату C: "))
    region = classify_point(x, y, c)
    print(f"Точка ({x:.1f}, {y:.1f})  попадает в область {region}.")


if __name__ == "__main__":
    main()
