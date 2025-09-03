total_sum = 0

for num in range(31, 100):
    if num % 3 == 0 and str(num)[-1] in "248":
        total_sum += num


print(total_sum)
