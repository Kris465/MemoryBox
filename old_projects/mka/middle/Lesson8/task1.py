num_spels = int(input("Введите количество заклинаний: "))
spells = []

for i in range(num_spels):
    name = input("Введите название заклинания: ")
    power = int(input(f"Введите мощность заклнинания {name}: "))
    spells.append((name, power))

print("Заклинания с мощностью от 50 до 100: ")
for spell in spells:
    if 50 < spell[1] < 100:
        print(spell[0])
