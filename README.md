# Игра "Кто я?"

Задача 1: Создайте новый проект в PyCharm. 

Задача 2: Напишите основной код игры в main.py:

```python
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
```

Задача 3: Создайте отдельные файлы для каждого класса и не забудьте,  что названия классов пишется с большой буквы:

```python
class Animal:
    def __init__(self, name):
        self.name = name
```

```python
class Fruit:
    def __init__(self, name):
        self.name = name
```

Задача 4: Запустите код и проверьте работает ли он. 

Задача 5: Создайте еще свои пять классов. Внесите необходимые изменения в основной код, чтобы игра полноценно работала. 

Задача 6: Поиграйте с противоположной командой.
