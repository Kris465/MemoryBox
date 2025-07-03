from random import randint


chislo = randint(1, 100)
user_chislo = 0

while chislo != user_chislo:
    user_chislo = int(input("Введите число: "))
    if chislo > user_chislo:
        print("Больше!")
    else:
        print("Меньше!")

print("Вы угадали число!")
