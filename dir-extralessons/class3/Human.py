class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def main_info(self):
        print(f"Hello! My name is {self.name}"
              f"and I'm {self.age} years old")
        
nataly = Human("Nataly", 18)
nataly.main_info()
print(nataly.name)
print(nataly.age)
