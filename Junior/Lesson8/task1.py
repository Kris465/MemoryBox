def display_heroes(heroes):
    for name, power in heroes.items():
        print(f"Супергерой {name} имеет суперсилу {power}")


heroes = {
    "Супермен": "Летать",
    "Бетмен": "Интеллект",
    "Чудо-женщина": "Сила"
}

display_heroes(heroes)
