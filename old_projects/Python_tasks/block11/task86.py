weight_of_people = [60.6, 40.5, 36.7, 79.6, 115.5, 125.7, 70.6, 81.5, 75.7,
                    134.6, 34.5, 46.7, 85.6, 138.5, 30.7, 70.6, 86.5, 101.7,
                    65.6, 64.5, 42.7, 48.6, 67.5, 26.7, 108.5]

sum_fat = 0
sum = 0

count_fat = 0
count = 0

for i in weight_of_people:
    if i < 100:
        sum += i
        count += 1
    else:
        sum_fat += i
        count_fat += 1

avarage_fat = sum_fat / count_fat
avarage = sum / count

print(f'Средний вес полных людей - {avarage_fat}')
print(f'Средний вес остальных людей - {avarage}')
