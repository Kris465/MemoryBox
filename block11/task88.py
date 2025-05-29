import random

auto = random.randint(5000, 100000)
print(f"Цена автомобиля (случайно выбранная): {auto}")

moto = random.randint(1, 4999)

def result(auto, moto):
    print(f"\nТекущее значение цены автомобиля (выбрано случайно): {auto}")
    print(f"Текущее значение цены мотоцикла (выбрано случайно): {moto}\n")
    
    autoo = auto + auto // 2  # то есть 1.5 * auto
    print(f"Значение для нескольких авто (авто + половина авто): {autoo}")
    
    motoo = moto + moto  # то есть 2 * moto
    print(f"Значение для нескольких мотоциклов (мото + мото): {motoo}\n")
    
    if autoo < motoo * 3:
        print("Да, средняя стоимость авто менее чем в 3 раза больше стоимости мотоцикла")
    else:
        print("Нет, средняя стоимость авто не менее чем в 3 раза больше стоимости мотоцикла")
    
    return autoo, motoo

autoo, motoo = result(auto, moto)

while motoo * 3 != autoo:
    motoo += moto
    
    moto += 1
    
    print(f"Обновленная сумма цен мотоциклов: {motoo}")
    
print("Сумма цен мотоциклов теперь равна тройной стоимости авто.")