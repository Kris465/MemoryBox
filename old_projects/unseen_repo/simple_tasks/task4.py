import random
import string


def password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters)for _ in range(length))
    return password


try:
    length = int(input("Введите длину пароля (минимальное 8 символов): "))
    if length < 8:
        print("Пароль слишком короткий.")
    else:
        password = password(length)
        print(f"\nСгенерировать пароль: {password}")
        print("Не забудьте сохранить пароль")
except ValueError:
    print("Ошибка: введите целое число для длины пороля.")
