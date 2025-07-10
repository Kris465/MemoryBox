from random import randint


print("Привет! Я Дракоша Тоша, и я загадал число от 1 до 5. Попробуй угадать!")
secret = randint(1, 5)
guess = int(input("Твой вариант: "))

if guess == secret:
    print("Ура! Ты угадал! Тоша доволен!")
else:
    print(f"Ой-ой, не угадал! Тоша загадал число {secret}")
