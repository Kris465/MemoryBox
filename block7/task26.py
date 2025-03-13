Temperatyra = [12, 7, 3, 2, 0, -2, -6, 4, 15, -13, 5, 2, 0, -3, -34, 45]

count_temp = sum(1 for temp in Temperatyra if temp < 0)
print("Количество дней с темп ниже 0:", count_temp)
