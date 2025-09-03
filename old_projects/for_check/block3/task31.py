N = int(input("Введите число: "))

primer_one = (N % 5 == 0) or (N % 7 == 0)
primer_two = (N % 4 == 0) and (N % 10 != 0)

print(f"а) {primer_one}")
print(f"б) {primer_two}")
