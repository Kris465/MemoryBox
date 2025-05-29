precipitation = [50, 40, 60, 55, 45, 70, 65, 80, 75, 60, 55, 90]


months_indices = [2, 5, 8, 11]


total_precipitation = sum(precipitation[i] for i in months_indices)

print("Общее число осадков в марте, июне, сентябре и декабре:", /
      total_precipitation)
