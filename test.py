# a = [['_', '_', '_'],['_', '_', '_'],['_', '_', '_'],['_', '_', '_'],['_', '_', '_'],['_', '_', '_'],['_', '_', '_'],['_', '_', '_']]

# [print(i) for i in a]
from random import randint

# field = [["*" for j in range(5)] for i in range(5)]

# print(field)

def ran(size):
    return randint(0, size-1)

size = 10
a = []
[a.append(['_'] * size) for _ in range(size)]
player = 'X'
generate = [ran(size), ran(size)]
a[generate[0]][generate[1]] = player
[print(i) for i in a]
