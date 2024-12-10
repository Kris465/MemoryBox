def sherlock_skills():
    skills = {
        "Шерлок Холмс": ["Логическое мышление",
                         "Наблюдательность",
                         "Дедукция"],
        "Доктор Ватсон": ["Медицинские знания",
                          "Смелость"]
    }

    character = input("Введите имя персонажа(Шерлок Холмс и Доктор Ватсон): ")
    if character in skills:
        print(f"Суперспособности {character}: {", ".join(skills[character])}")
    else:
        print("Персонаж не найден.")


sherlock_skills()
