name = input("Введите имя:")
surname = input("Введите фамилию: ")
gudgets = []

while True:
    gudget = input("Введите крутой гаджет Бетмена или exit: ")
    gudgets.append(gudget)
    if gudget == 'exit':
        break

print(f"{name} {surname} любит {gudgets}")
with open('hooray.txt', 'a', encoding='UTF-8') as file:
    file.write(f"{name} {surname} любит {gudgets}")
