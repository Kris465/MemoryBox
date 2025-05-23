precipitation = [10, 5, 0, 8, 12, 3, 7, 4, 6, 9, 2, 11,
                 0, 4, 8, 5, 3, 7, 2, 6, 9, 1, 4, 10,
                 3, 5, 2, 8]

total_precip_even_days = sum(precipitation[i] for i in range(1, len(precipitation), 2))

print("Общее число осадков по четным числам февраля:", total_precip_even_days)
