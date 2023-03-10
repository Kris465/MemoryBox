import os


from Player import Player


class Field:

    @property
    def size(self):
        return self._size

    @property
    def field(self):
        return self._field

    def __init__(self, size=10):
        self._field = [['-'] * size for _ in range(size)]
        self._size = size


