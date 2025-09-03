n = int(input("Введите количество городов: "))
distances = []

for i in range(n):
    distance = float(input(f"Введите расстояние до города {i + 1}: "))
    distances.append(distance)
max_distance = max(distances)

print(f"Расстояние до самого удаленного города: {max_distance} км")
