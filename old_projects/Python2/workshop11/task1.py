# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания
# (time.time)


import time


class MyString(str):
    """
    Класс MyString наследуется от str и дополнительно хранит имя автора строки и время создания.
    """

    def __new__(cls, value, author):
        obj = str.__new__(cls, value)
        obj.author = author
        obj.time_created = time.time()
        return obj

    def __repr__(self):
        return f"MyString({super().__repr__()}, author={self.author}, time_created={self.time_created})"

    def __str__(self):
        """
        Метод возвращает строковое представление объекта.
        """
        return f"Строка: {self}\nАвтор: {self.author}\nВремя создания: {self.time_created}"


s = MyString("Hello, world!", "John")
print(s)
