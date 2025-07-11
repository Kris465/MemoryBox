diamonds = input("Сколько алмазов у Стива?")

if diamonds.isdigit():
    diamonds = int(diamonds)
    print(f"Теперь у Стива {diamonds} алмазов... пока их не украл Эндермен!")
else:
    print("Крипер шипит: 'Тссс... это не цифра!'")
