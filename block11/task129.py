ages = [25, 30, 22, 35, 22, 40, 40]

min_age = min(ages)
min_index = ages.index(min_age)

max_age = max(ages)
max_index = ages.index(max_age)

if min_index < max_index:
    print("Самый молодой человек встречается раньше.")
elif max_index < min_index:
    print("Самый старый человек встречается раньше.")
else:
    print("Самые молодой и старый человек встречаются одновременно.")
