mice = int(input("Введите количество мышей: "))
mice_caught = []

for i in range(mice):
    mouse_name = input(f"Введите имя мыши {i + 1}: ")

    mice_caught.append(mouse_name)

print("Мурзик поймал следующих мышей:", *mice_caught)
