num_superheroes = int(input("Введите количество супергероев: "))
superheroes = []
heroes_sum = 0

for i in range(num_superheroes):
    name = input("Введите имя супергероя: ")
    power = int(input(f"Введите силу {name}: "))
    superheroes.append((name, power))

print("Супергерои от 80 ")
for hero in superheroes:
    if 80 < hero[1]:
        print(hero[0])
        heroes_sum += 1

print(f"Всего героев с силой, больше 80: {heroes_sum}")
