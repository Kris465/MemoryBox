def characters_by_cartoon():
    cartoons = {
        "Король Лев": ["Мафусаил", "Симба", "Нала"],
        "Холодное сердце": ["Эльза", "Анна", "Олаф"],
        "Тачки": ["Молния Маквин", "Док Худ", "Салли"],
    }

    cartoon = input("Введите название мультфильма: ")
    if cartoon in cartoons:
        print("Персонажи:", ", ".join(cartoons[cartoon]))
    else:
        print("Извините, я не знаю этот мультфильм.")


characters_by_cartoon()
