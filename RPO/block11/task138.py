temperatures = [12, 30, 61, 20, 34, 12, 11, 1, 2, 5, 6, 7, 9, 20, 27]

max_temp = float('-inf')
second_max_temp = float('-inf')
max_day = -1
second_max_day = -1

for i, temp in enumerate(temperatures, start=1):
    if temp > max_temp:
        second_max_temp = max_temp
        second_max_day = max_day
        max_temp = temp
        max_day = i
    elif temp > second_max_temp and temp != max_temp:
        second_max_temp = temp
        second_max_day = i

print("Даты двух самых теплых дней:", max_day, second_max_day)
