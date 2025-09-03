def wizard_spells():
    name = input("Введите имя волшебника: ")
    spells = input("Введите заклинания через запятую: ").split(",")
    spells = [spell.strip() for spell in spells]
    known_spells = []

    while True:
        spell_to_check = input("введите заклинание для проверки (или 'стоп' для выхода): ")
        if spell_to_check.lower() == 'стоп':
            break
        if spell_to_check in spells:
            print(f"{name} знает заклинание {spell_to_check}")

            known_spells.append(spell_to_check)
        else:
            print(f"{name} не знает заклинание {spell_to_check}.")

    print(f"\nИзвестные заклинания {name}: {",".join(known_spells)}")


wizard_spells()
