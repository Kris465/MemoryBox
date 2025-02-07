def get_day_of_week(k):
    days = ["Ponedelnik", "Vtornik", "Sreda", "Chetverg",
            "Pyatnitsa", "Subbota", "Voskresenie"]
    if not (1 <= k <= 365):
        print("Число должно быть от 1 до 365")
        return
    day_index = k % 7
    print(days[day_index])


k = int(input("Введите целое число (1<=k<=365)"))
get_day_of_week(k)
