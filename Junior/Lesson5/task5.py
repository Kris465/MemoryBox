name = input("Введите имя:")
surname = input("Введите фамилию: ")
mood = input("Введите настроение Халка!")
with open('hulk_mood.txt', 'a', encoding='UTF-8') as file:
    file.write(f"Осторожно! {name} {surname}, Халк {mood}!")
