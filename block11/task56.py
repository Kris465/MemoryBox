# Исходный массив
array = [1, 2, 3, 4, 5, 6, 7, 8]

# Инициализация суммы
sum_even_positions = 0

# Проходим по массиву и складываем элементы на четных позициях
for i in range(1, len(array), 2):
    sum_even_positions += array[i]

print("Сумма элементов на вторых, четвертых, шестых и т.д. позициях:",
      sum_even_positions)
