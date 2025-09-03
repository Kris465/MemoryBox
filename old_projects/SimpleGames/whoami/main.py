import random
from animal import Animal
from fruit import Fruit

animals = [Animal("Собака"), Animal("Кошка"), Animal("Лев")]
fruits = [Fruit("Яблоко"), Fruit("Банан"), Fruit("Апельсин")]

# Список всех объектов
objects = animals + fruits


def play_game():
    # Выбираем случайный объект из списка
    random_object = random.choice(objects)

    print("Угадайте, к какому классу относится объект:")
    print(f"Название объекта: {random_object.name}")

    user_guess = input("Введите 'animal' или 'fruit': ")

    # Проверяем ответ игрока
    if (isinstance(random_object, Animal) and user_guess.lower() == "animal") or \
       (isinstance(random_object, Fruit) and user_guess.lower() == "fruit"):
        print("Правильно!")
    else:
        print("Неправильно. Попробуйте еще раз.")


# Играем до тех пор, пока игрок не введет "exit"
while True:
    play_game()
    play_again = input("Хотите сыграть еще раз? (y/n): ")
    if play_again.lower() != "y":
        break
