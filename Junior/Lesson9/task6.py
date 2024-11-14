num_locations = int(input("Сколько мест капитан Джек посетил?"))
locations = []

for i in range(num_locations):
    location_name = input(f"Введите имя места {i + 1}: ")
    locations.append(location_name)

for location in locations:
    found_treasure = input(
        f"Капитан Джек нашел сокровища на {location}? (да/нет): ")
    if found_treasure.lower() == "да":
        print(f"На {location} сокровища найдены")
    else:
        print(f"На {location} сокровищ нет")
