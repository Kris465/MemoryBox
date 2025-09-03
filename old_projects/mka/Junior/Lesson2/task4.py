def count_characters():
    cartoons = {
        "Покахонтас": ["Покахонтас", "Джон Смит", "Мэти"],
        "Аладдин": ["Аладдин", "Жасмин", "Джин"],
    }

    cartoon = input("Введите название мультфильма: ")
    if cartoon in cartoons:
        print(f"Количество персонажей в '{cartoon}': {len(cartoons[cartoon])}")
    else:
        print("Извините, я не знаю этот мультфильм.")


count_characters()
