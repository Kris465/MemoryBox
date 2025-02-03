from interface import create_interface
from loguru import logger


def main():
    try:
        user_data = create_interface()
    except Exception as e:
        logger.error(e)

    print("Польовательские данные:", user_data)


if __name__ == "__main__":
    main()
