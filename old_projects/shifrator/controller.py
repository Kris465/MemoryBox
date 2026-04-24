from datetime import datetime
from loguru import logger
from cryptography.fernet import Fernet
from view import user_menu, answer_with_result
from model import write, read


def controller():
    """
    data = {"date": result}
    """
    logger.info("Контроллер создан")

    KEY = Fernet.generate_key()
    cipher = Fernet(KEY)

    while True:
        data = read()
        line = user_menu()
        logger.info(f"В переменной line: {line}")
        if line[1] == 1:
            result = encrypt(line[0], cipher)
            answer_with_result(result)
        elif line[1] == 2:
            result = decrypt(line[0], cipher)
            answer_with_result(result)
        elif line[1] == 3:
            return
        else:
            logger.error("Пользователь выбрал не 1 и не 2!")

        data.update({f"{datetime.now()}": result})
        write(data)

def encrypt(text, cipher):
    return cipher.encrypt(text.encode()).decode()


def decrypt(text, cipher):
    return cipher.decrypt(text.encode()).decode()
