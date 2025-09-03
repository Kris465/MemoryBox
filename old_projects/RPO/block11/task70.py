def input_results():
    data = input("Введите результаты 20 игр (\
        3 — победа, 1 — ничья, 0 — проигрыш), разделённые пробелом: ")
    results = [int(x) for x in data.strip().split()]
    if len(results) != 20:
        print("Ошибка: необходимо ввести ровно 20 результатов.")
        return None
    return results


def main():
    results = input_results()
    if results is None:
        return

    wins = sum(1 for r in results if r == 3)
    draws = sum(1 for r in results if r == 1)

    print(f"Общее количество побед: {wins}")
    print(f"Общее количество ничьих: {draws}")


if __name__ == "__main__":
    main()
