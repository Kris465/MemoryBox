result = []


num = 107

while len(result) < 10:

    if num % 9 == 0:
        result.append(num)

    num += 10

print("Первые 10 натуральных чисел, удовлетворяющих условиям:", result)
