import math
array = [4, 9, 16, 25, 36]
# Выберите индекс элемента, из которого нужно взять квадратный корень
index = int(input("Введите индекс элемента массива для вычисления его \
                  квадратного корня: "))

if 0 <= index < len(array):
    element = array[index]
    if element >= 0:
        sqrt_value = math.sqrt(element)
        print(f"Квадратный корень из элемента {element} равен {sqrt_value}")
    else:
        print("Невозможно вычислить квадратный корень из отрицательного \
              числа.")
else:
    print("Некорректный индекс.")

index1 = int(input("Введите индекс первого элемента: "))
index2 = int(input("Введите индекс второго элемента: "))

if (0 <= index1 < len(array)) and (0 <= index2 < len(array)):
    elem1 = array[index1]
    elem2 = array[index2]
    average = (elem1 + elem2) / 2
    print(f"Среднее арифметическое элементов {elem1} и {elem2} \
          равно {average}")
else:
    print("Один или оба индекса некорректны.")
