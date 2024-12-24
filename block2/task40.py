y = float(input("Введите число полных часов: "))
hours = int(y // 30)
minutes = int((y % 30) * 2)
print(f"Часы: {hours}. Минуты: {minutes}")
