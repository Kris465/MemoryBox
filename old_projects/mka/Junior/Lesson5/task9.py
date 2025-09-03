name = input("Введите имя:")
surname = input("Введите фамилию: ")
qualities = []

while True:
    quality = input("Введите любимую цитату или exit: ")
    qualities.append(quality)
    if quality == 'exit':
        break

print(f"{name} {surname} считает, что Чудо Женщина обладает {qualities}")
with open('wonderwoman.txt', 'a', encoding='UTF-8') as file:
    file.write(f"{name} {surname} любит {qualities}")
