seconds = int(input("Введите количество секунд: "))

hours = seconds // 3600
minutes = (seconds - hours * 3600) // 60
seconds = seconds - hours * 3600 - minutes * 60

print(f"{hours} часов {minutes} минут {seconds} секунд")
