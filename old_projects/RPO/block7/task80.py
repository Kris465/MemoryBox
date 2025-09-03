n = int(input("Введите количество покупателей: "))
t = list(map(float, input("Введите время обслуживания\
    для каждого покупателя через пробел: ").split()))

wait_times = []
min_time = float('inf')
min_index = -1

for i in range(n):
    wait_time = (i + 1) * t[i]
    wait_times.append(wait_time)
    if wait_time < min_time:
        min_time = wait_time
        min_index = i + 1

print(f"Времена пребывания покупателей в очереди: {wait_times}")
print(f"Номер покупателя,\
    для обслуживания которого требуется самое малое время: {min_index}")
