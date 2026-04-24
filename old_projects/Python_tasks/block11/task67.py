def input_sales():
    data = input("Введите стоимости товаров за каждый день марта, разделённые пробелом: ")
    sales = [float(x) for x in data.strip().split()]
    if len(sales) != 31:
        print("Ошибка: необходимо ввести ровно 31 значение.")
        return None
    return sales


def main():
    sales = input_sales()
    if sales is None:
        return
    s = float(input("Введите значение s: "))
    count_days = sum(1 for x in sales if x > s)
    print(f"Количество дней, когда стоимость превысила {s}: {count_days}")


if __name__ == "__main__":
    main()
