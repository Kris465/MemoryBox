scores = [8.5, 9.0, 8.7, 9.2, 8.8, 9.1,
          8.9, 9.3, 9.0, 8.7, 9.1, 8.8,
          9.2, 8.9, 9.1, 8.7, 9.0, 8.8]

mandatory_sum = sum(scores[:6])
short_program_sum = sum(scores[6:12])
free_program_sum = sum(scores[12:])

max_sum = max(mandatory_sum, short_program_sum, free_program_sum)

if max_sum == mandatory_sum:
    print("Лучший результат по обязательной программе.")
elif max_sum == short_program_sum:
    print("Лучший результат по короткой программе.")
else:
    print("Лучший результат по произвольной программе.")