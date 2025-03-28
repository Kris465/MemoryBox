n = 5
a = [1, 2, 3, 4, 5]


alternating_sum_result = sum(a[i] * (-1) ** i for i in range(n))
print("a) Результат: ", alternating_sum_result)


sum_first_last_result = a[0] + a[-1]
print("б) Результат: ", sum_first_last_result)


difference_first_second_result = a[0] - a[1]
print("в) Результат: ", difference_first_second_result)
