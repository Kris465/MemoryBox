snezinki = input("Сколько печенек съел Бэтмен?")

if snezinki.isdigit():
    snezinki = int(snezinki)
    print(f"Теперь в Аренделле {snezinki} метель! ❄️")
else:
    print("Джокер смеётся: 'Ха-ха, ты не умеешь считать!'")
