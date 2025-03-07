def count_fives(grades):
    # Бинарный поиск для нахождения первого элемента, не равного "5"
    left, right = 0, len(grades)
    while left < right:
        mid = (left + right) // 2
        if grades[mid] != "5":
            right = mid
        else:
            left = mid + 1
    return left

# Список оценок, где сначала идут все "5", а затем остальные оценки
grades = ["5", "5", "5", "5", "5", "4", "3", "4", "2", "5", "5", "5", "5", "5", "5", "5", "5", "5", "5", "5"]

# Случай 1: известно, что пятерки имеют не все ученики класса
if grades[-1] != "5":
    count = count_fives(grades)
    print(f"Количество учеников с оценкой '5': {count}")
else:
    # Случай 2: допускается, что пятерки могут иметь все ученики класса
    if all(grade == "5" for grade in grades):
        print("Все ученики имеют оценку '5'")
    else:
        count = count_fives(grades)
        print(f"Количество учеников с оценкой '5': {count}")
