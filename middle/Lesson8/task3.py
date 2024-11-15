num_animals = int(input("Введите количество животных: "))
police_officers = []
heroes_sum = 0

for i in range(num_animals):
    name = input("Введите имя животного: ")
    role = input("Введите роль (полицейский/преступник): ").lower()

    if role == "полицейский":
        is_mammal = input(f"{name} является млекопитающим? (да/нет): ").lower()
        police_officers.append((name, is_mammal))

print("nСписок полицейских:")
for officer in police_officers:
    print(officer[0])

for officer in police_officers:
    if officer[1] == "да":
        heroes_sum += 1

print(f"Количество полицейских, которые являются млекопитающими: {heroes_sum}")
