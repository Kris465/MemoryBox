def compare_sets():
    print("Введите стоимость предметов первого набора:")
    set1 = [float(input()) for _ in range(8)]

    print("\nВведите стоимость предметов второго набора:")
    set2 = [float(input()) for _ in range(8)]

    total_set1 = sum(set1)
    total_set2 = sum(set2)

    if total_set1 < total_set2:
        print("Первый набор дешевле.")
    elif total_set1 > total_set2:
        print("Второй набор дешевле.")
    else:
        print("Стоимость наборов одинакова.")


compare_sets()
