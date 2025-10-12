from dotenv import load_dotenv, find_dotenv
from loguru import logger
from src.downloader.stepik_downloader import StepikDownloader
from src.utils import url_parser


# Настройка логов
logger.add("logs/stepik_downloader.log", rotation="10 MB", level="INFO")


def main():
    # Загружаем переменные окружения
    load_dotenv(find_dotenv())
    logger.info("Запуск Stepik AI Assistant")
    try:
        # Создаем экземпляр загрузчика
        downloader = StepikDownloader()

        # Получаем данные от пользователя
        course_url = input("Введите ссылку на курс Stepik: ").strip()
        weeks_input = input("Сколько недель обработать? (оставьте пустым для всех): ").strip()

        weeks_to_process = int(weeks_input) if weeks_input else None

        # Запускаем скачивание
        downloader.download_course_videos(
            course_url=course_url,
            weeks_to_process=weeks_to_process,
            quality="720"
        )

    except Exception as e:
        logger.error(f"Ошибка в работе приложения: {e}")


if __name__ == "__main__":
    main()
