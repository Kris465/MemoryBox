name = input("Введите имя:")
surname = input("Введите фамилию: ")
numbers = int(input("Введите сколько раз хотите повторить фразу 'Cупергерой!'"))
num = 0
while num < numbers:
    with open('hooray.txt', 'a', encoding='UTF-8') as file:
        file.write(f"{name} {surname} кричит 'Cупергерой!'")
        num += 1
