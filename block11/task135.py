results = [10.5, 10.2, 10.8, 9.9, 10.1, 10.3, 9.8, 10.0, 10.4, 9.7,
           10.6, 10.9, 9.6, 10.7, 10.2, 9.5, 10.3, 9.4, 10.1, 9.3,
           10.0, 9.2]


best_time = float('inf')
second_best_time = float('inf')

for time in results:
    if time < best_time:
        second_best_time = best_time
        best_time = time
    elif best_time < time < second_best_time:
        second_best_time = time

print("Лучшее время (1 место):", best_time)
print("Второе место:", second_best_time)
