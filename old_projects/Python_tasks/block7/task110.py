precipitation_data = [0, 2, 0, 5, 0, 3, 0, 0, 1, 0, 0, 0, 2,
                      0, 4, 0, 0, 3, 0, 1,
                      0, 0, 0, 2, 0, 0, 0, 5, 0, 0, 0]


def check_no_precipitation_days(precipitation_data):
    count_zero_days = 0

    for day in precipitation_data:
        if day == 0:
            count_zero_days += 1

    return count_zero_days == 10


if check_no_precipitation_days(precipitation_data):
    print("Осадков не было ровно 10 дней в месяце.")
else:
    print("Осадков не было не ровно 10 дней в месяце.")
