from random import choice


user = input("Введите свой выбор(камень, ножницы, бумага): ")
spicok = ["камень", "ножницы", "бумага"]
computer = choice(spicok)
print(computer)

if user == "камень" and computer == "ножницы":
    print("user победил")
elif user == "ножницы" and computer == "камень":
    print("computer победил")
elif user == "ножницы" and computer == "бумага":
    print("user победил")
elif user == "бумага" and computer == "ножницы":
    print("computer победил")
elif user == "камень" and computer == "бумага":
    print("computer победил")
elif user == "камень" and computer == "камень":
    print("ничья")
elif user == "ножницы" and computer == "ножницы":
    print("ничья")
elif user == "бумага" and computer == "бумага":
    print("ничья")
