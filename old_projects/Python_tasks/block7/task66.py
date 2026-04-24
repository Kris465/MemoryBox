class_sizes = []


for i in range(20):
    size = int(input(f"Введите численность учеников в классе {i + 1}: "))
    class_sizes.append(size)


max_size = max(class_sizes)
min_size = min(class_sizes)


difference = max_size - min_size


print(f"Численность самого большого класса превышает численность самого маленького класса на {difference} учеников.")
