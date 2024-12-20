n = int(input("сколько игроков в команде бублик: "))
count = 0
goals = 0
for i in range(n):

    surname = input("какая фамилия у вашего игрока?:")
    name = input("какое имя у вашего игрока?:")
    birth_year = int(input("какого года рождение ваш игрок?:"))
    goal = int(input("сколько голов у игрока:"))

    if 1998 <= birth_year <= 2000 and goals == 0:
        count += 1
        print(f'футболисты родившихся с 1998 по 2000 г\
 не забивают ни одного гола {count}')
