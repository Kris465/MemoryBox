cookies = input("Сколько печенек съел Бэтмен?")

if cookies.isdigit():
    cookies = int(cookies)
    print(f"Брюс Уэйн теперь весит на {cookies} кг больше. Назад в спортзал!")
else:
    print("Олаф говорит: 'Э-э-э... это не похоже на цифру!'")
