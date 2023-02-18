class Character:

    def __init__(self, name, hp):
        self.__name = name
        self.__hp = hp

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name

    
doctor = Character("Scary", 100)
doctor.name = "House"
print(doctor.name)
print(doctor.__dict__)


