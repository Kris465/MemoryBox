import random
import string

def password_generator():
    length = int(input("Введите длину пароля: "))
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    
    print(f"Сгенерированный пароль: {password}")

password_generator()
