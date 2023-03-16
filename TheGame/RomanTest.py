


from random import randint
size = 10
lst = [randint(0, size-1) for i in range(10)]
a = []

[a.append(['_'] * size) for _ in range(size+1)]

player = 'X'
mina1 = '*'
mina2 = '*'
swamp1 = '~'
swamp2 = '~'
health1 = '$'
health2 = '$'

a[lst[0]][lst[7]] = player
a[lst[1]][lst[8]] = mina1
a[lst[2]][lst[9]] = mina2
a[lst[3]][lst[8]] = swamp1
a[lst[4]][lst[7]] = swamp2
a[lst[5]][lst[6]] = health1
a[lst[6]][lst[5]] = health2
[print(i) for i in a]