import random

def adventure(hero, adventures):
    chosen_adventure = random.choice(adventures)
    return f"{hero} отправился в приключение: {chosen_adventure}"


adventure = ["Спасение города", "Битва с врагами", "Поездка в космос"]
print(adventure("Супермен", adventures))
