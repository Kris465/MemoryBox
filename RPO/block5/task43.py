sequence = []
num = int(input("Введите число: "))
while num != 1000:
    sequence.append(num)
    num = int(input("Введите число: "))

unique_numbers = set(sequence)
count_repeats = sum(sequence.count(x) > 1 for x in unique_numbers)

distinct_count = len(unique_numbers)

print(f"Количество повторяющихся чисел: {count_repeats}")
print(f"Количество различных чисел: {distinct_count}")
