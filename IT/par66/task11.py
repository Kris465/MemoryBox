n = int(input("Количество игроков: "))
goals = 0
count = 0
players = {}

for i in range(n):
    familiya = input("Фамилия игрока: ")
    imya = input("Имя игрока: ")
    goals = int(input("Кол-во голов игрока: "))
    players.update({familiya + imya: goals})

temp = ['', 0]
for key, value in players.items():
    if temp[1] < value:
        temp = [key, value]

print(temp)
