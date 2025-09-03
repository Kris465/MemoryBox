import random


def battle(hero1, hero2):
    winner = random.choice([hero1, hero2])
    return f"Победитель: {winner}"


hero1 = input("Введите имя первого супергероя: ")
hero2 = input("Введите имя второго супергероя: ")
print(battle(hero1, hero2))
