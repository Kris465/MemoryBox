A = int(input("Введите число: "))

primer_one = (A % 2 == 0) or (A % 3 == 0)
primer_two = (A % 3 == 1) and (A % 10 == 0)

print(f"{primer_one, primer_two}")
