mushrooms = input("Сколько грибов собрал Марио?")

if mushrooms.isdigit():
    mushrooms = int(mushrooms)
    print(f"Марио теперь на {mushrooms} см выше! (Но всё равно не догонит Соника)")
else:
    print("Луиджи говорит: 'Это не число, дружок-пирожок!'")
