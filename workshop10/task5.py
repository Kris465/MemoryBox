# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.


class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        print("Я животное, меня зовут", self.name)


class Fish(Animal):
    def __init__(self, name, habitat):
        super().__init__(name)
        self.habitat = habitat

    def info(self):
        print("Я рыба, меня зовут", self.name, "и я обитаю в", self.habitat)


class Bird(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan

    def info(self):
        print("Я птица, меня зовут", self.name,
              "и мой размах крыльев составляет", self.wingspan, "см")


class Mammal(Animal):
    def __init__(self, name, diet):
        super().__init__(name)
        self.diet = diet

    def info(self):
        print("Я млекопитающее, меня зовут", self.name,
              "и я питаюсь", self.diet)


fish = Fish("Карась", "пруду")
bird = Bird("Сокол", 80)
mammal = Mammal("Лев", "мясом")

fish.info()
bird.info()
mammal.info()
