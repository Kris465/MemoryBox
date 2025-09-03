# Массив с количеством осадков за каждый день июня (30 дней)
# Замените на свои данные при необходимости
precipitation = [5, 3, 0, 2, 4, 6, 1, 0, 2, 3,
                 4, 5, 2, 1, 0, 3, 4, 2, 1, 0,
                 3, 4, 5, 2, 1, 0, 3, 4, 2, 1]

# а) Сравнить сумму осадков в первую и вторую половину июня
first_half = precipitation[:15]   # дни с 1 по 15
second_half = precipitation[15:]

sum_first_half = sum(first_half)
sum_second_half = sum(second_half)

if sum_first_half > sum_second_half:
    print("В первую половину июня выпало больше осадков.")
elif sum_first_half < sum_second_half:
    print("Во вторую половину июня выпало больше осадков.")
else:
    print("Количество осадков в первую и вторую половины июня равно.")


decade1 = precipitation[:10]
decade2 = precipitation[10:20]
decade3 = precipitation[20:]

sum_decade1 = sum(decade1)
sum_decade2 = sum(decade2)
sum_decade3 = sum(decade3)

max_sum = max(sum_decade1, sum_decade2, sum_decade3)

if max_sum == sum_decade1:
    print("Больше всего осадков выпало в первую декаду месяца.")
elif max_sum == sum_decade2:
    print("Больше всего осадков выпало во вторую декаду месяца.")
else:
    print("Больше всего осадков выпало в третью декаду месяца.")
