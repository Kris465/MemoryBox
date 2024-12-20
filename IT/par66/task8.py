file = input("Введите имя файла: ")
ending = input("Введите новое расширение: ")
if "." not in file:
    print(file + "." + ending)
else:
    i = -1
    while file[i] != '.':
        (file + ending)
