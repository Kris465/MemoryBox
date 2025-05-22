# Ввод исходного массива (рост учеников)
growths = list(map(int, input("Введите рост 25 учеников\
    через пробел: ").split()))
if len(growths) != 25:
    print("Ошибка: необходимо ввести ровно 25 значений.")
    exit()

# Ввод значений роста выбывших учеников
lost_values = list(map(int, input("Введите рост выбывших учеников \
    через пробел (2 значения): ").split()))
if len(lost_values) != 2:
    print("Ошибка: необходимо ввести два значения роста.")
    exit()

# Удаляем по значениям роста
remaining = growths.copy()
for val in lost_values:
    if val in remaining:
        remaining.remove(val)
    else:
        print(f"Значение {val} не найдено среди оставшихся.")

print("Обновленный массив роста:", remaining)
