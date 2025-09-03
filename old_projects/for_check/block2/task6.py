n = int(input("Введите секунды:"))

hours_passed = round(n / 3600)
minutes_passed = round((n % 3600) / 60)
seconds_passed = round(n % 60)

print(f"Часов прошло:{hours_passed}")
print(f"Минут прошло:{minutes_passed}")
print(f"Секунд прошло:{seconds_passed}")
