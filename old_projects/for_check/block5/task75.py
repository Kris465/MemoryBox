current_power = 2 * 2


total_sum = current_power


for _ in range(3, 11):
    current_power *= 2
    total_sum += current_power


print(total_sum)
