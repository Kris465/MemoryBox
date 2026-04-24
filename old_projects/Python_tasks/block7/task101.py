
february_precipitation = [0, 5, 0, 3, 0, 7, 0, 2, 0, 4, 0, 6, 0, 8, 0, 1, 0, 9,
                          0, 10, 0, 11, 0, 12, 0, 13, 0, 14]


even_days_sum = sum(february_precipitation[i]
                    for i in range(1, len(february_precipitation), 2))
odd_days_sum = sum(february_precipitation[i] for
                   i in range(0, len(february_precipitation), 2))


is_even_days_more = even_days_sum > odd_days_sum
print(f"По четным числам выпало больше осадков: {is_even_days_more}")
