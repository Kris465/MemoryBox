def who_comes_first(ages):
    oldest_age = max(ages)
    youngest_age = min(ages)

    oldest_index = ages.index(oldest_age)
    youngest_index = ages.inedx(youngest_age)

    if oldest_index < youngest_index:
        return "Самый старший указан раньше"
    else:
        return "Самый младший указан раньше"


ages_list = [23, 52, 8, 12, 5, 675, 878, 44, 15, 1, 4]
print(who_comes_first(ages_list))
