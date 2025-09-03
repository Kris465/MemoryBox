def best_hero(heroes):
    return max(heroes, key=heroes.get)


hero_rating = {
    "Супермен": 95,
    "Бэтмен": 85,
    "Чудо-женщина": 90
}


print(f"Лучший супергерой {best_hero(hero_rating)}")
