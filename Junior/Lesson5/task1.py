name = input("Введите имя:")
surname = input("Введите фамилию: ")
selected_faculty = input("Введите название факультета:")
facultes = ["Гриффиндор", "Слизерин", "Хаффлпафф", "Равенкло"]
if selected_faculty in facultes:
    with open('hogwarts.txt', 'a') as file:
        file.write(f"{name} {surname} - Факультет: {selected_faculty}\n")
        print(f"Вы выбрали факультет {selected_faculty}")
else:
    print("Выбран неверный факультет.")
