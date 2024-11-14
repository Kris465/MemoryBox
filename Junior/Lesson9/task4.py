friends = input("Введите имена друзей Шарика через запятую: ").split()
friends = [friend.strip() for friend in friends]
if "Рекс" in friends:
    print("Шарик нашел рекса!")
else:
    print("Шарик не нашел Рекса")
