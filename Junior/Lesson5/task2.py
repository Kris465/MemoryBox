name = input("Введите имя:")
surname = input("Введите фамилию: ")
abilities = []
while True:
    ability = input("Введите вашу суперспособность или exit: ")
    abilities.append(ability)
    if ability == 'exit':
        break
print(f"{name} {surname} умеет {abilities}")
with open('abilities.txt', 'a', encoding='UTF-8') as file:
    file.write(f"{name} {surname} умеет {abilities}")
