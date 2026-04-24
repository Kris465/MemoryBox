numbers = [a1, a2, ..., an]


sum_less_than_20_5 = sum(num for num in numbers if num < 20.5)
is_sum_less_than_50 = sum_less_than_20_5 <= 50
print(is_sum_less_than_50)


sum_less_than_or_equal_10 = sum(num for num in numbers if num <= 10)
is_sum_multiple_of_3 = sum_less_than_or_equal_10 % 3 == 0
print(is_sum_multiple_of_3)
