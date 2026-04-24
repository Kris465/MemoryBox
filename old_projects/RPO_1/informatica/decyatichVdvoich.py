desat_chis = int(input("Введите число: "))
result = ""

while desat_chis > 0:
    result = str(desat_chis % 2) + result
    desat_chis = desat_chis // 2
    print(result)
