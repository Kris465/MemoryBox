N = int(input("Сколько у Тони мини-реакторов? Введите число: "))
max_popitok = 15
tecushuya_popitka = 1

while tecushuya_popitka <= max_popitok:
    if tecushuya_popitka <= N:
        print(f"Реактор {tecushuya_popitka} работает!")
    else:
        print(
            f"Тони, у тебя кончились реакторы на попытке: {tecushuya_popitka}")
    tecushuya_popitka += 1
