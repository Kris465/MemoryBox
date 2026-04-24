from loguru import logger
from view import view
from model import Database


def controller():
    db = Database()
    user_input = None
    while user_input != 2:
        user_input = view()
        logger.info(f"Пользователь ввел {user_input}")

        if isinstance(user_input, int):
            if user_input == 2:
                logger.info("Выход из программы")
                break
            else:
                # If user entered a number (not 2), store it in the database
                db.write_to_db(user_input)
                print(f"Число {user_input} записано в базу данных")

                # Read the latest number from database and display it
                latest_number = db.read_from_db()
                if latest_number is not None:
                    print(f"Последнее число из базы данных: {latest_number}")
        else:
            # Handle error message case
            print(user_input)  # Print error message
