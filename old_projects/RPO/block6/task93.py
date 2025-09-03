from random import randint


def count_consecutive_dry_days(rainfall):
    count = 0
    for day in rainfall:
        if day == 0:
            count += 1
        else:
            break
        return count


rainfall_case1 = [randint(0, 15) for i in range(15)]
print("Количество первых дней без осадков \
    (случай 1):", count_consecutive_dry_days(rainfall_case1))

rainfall_case2 = [randint(0, 0) for i in range(0)]
print("Количество первых дней без осадков (случай 2):",
      count_consecutive_dry_days(rainfall_case2))
