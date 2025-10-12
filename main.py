import sys
from dotenv import load_dotenv, find_dotenv
from loguru import logger
from src.downloader.stepik_downloader import StepikDownloader
from src.transcriber.whisper_transcriber import WhisperTranscriber

# Настройка логов
logger.add("logs/stepik_assistant.log", rotation="10 MB", level="INFO")


class StepikAIAssistant:
    def __init__(self):
        load_dotenv(find_dotenv())
        self.downloader = None
        self.transcriber = None

    def show_menu(self):
        """Главное меню"""
        print("\n" + "="*50)
        print("STEPIK AI ASSISTANT")
        print("="*50)
        print("1.Скачать видео с курса")
        print("2.Транскрибировать видео")
        print("3.Полный цикл (скачать + транскрибировать)")
        print("4.Выход")
        print("="*50)

    def get_course_info(self):
        """Получение информации о курсе"""
        print("\nВведите данные курса:")
        course_url = input("Ссылка на курс Stepik: ").strip()

        weeks_input = input("Сколько недель обработать? (оставьте пустым для всех): ").strip()
        weeks_to_process = int(weeks_input) if weeks_input else None

        quality = self.get_quality_choice()

        return course_url, weeks_to_process, quality

    def get_quality_choice(self):
        """Выбор качества видео"""
        print("\nВыберите качество видео:")
        print("1. 1080p (лучшее)")
        print("2. 720p (рекомендуется)")
        print("3. 360p (экономное)")

        choice = input("Ваш выбор (1-3, по умолчанию 2): ").strip()
        quality_map = {"1": "1080", "2": "720", "3": "360"}
        return quality_map.get(choice, "720")

    def get_transcribe_info(self):
        """Получение параметров транскрибации"""
        print("\nНастройки транскрибации:")

        # Выбор модели
        print("Выберите модель Whisper:")
        print("1. tiny (быстрая, низкое качество)")
        print("2. base (баланс скорости/качества)")
        print("3. small (хорошее качество)")
        print("4. medium (рекомендуется, высокое качество)")
        print("5. large (лучшее качество, медленная)")

        model_choice = input("Ваш выбор (1-5, по умолчанию 4): ").strip()
        model_map = {"1": "tiny", "2": "base", "3": "small", "4": "medium", "5": "large"}
        model_size = model_map.get(model_choice, "medium")

        # Выбор недель для транскрибации
        weeks_input = input("Какие недели транскрибировать? (через запятую, пусто = все): ").strip()
        if weeks_input:
            transcribe_weeks = [int(w.strip()) for w in weeks_input.split(",")]
        else:
            transcribe_weeks = None

        return model_size, transcribe_weeks

    def download_videos(self):
        """Опция 1: Скачивание видео"""
        print("\nЗАГРУЗКА ВИДЕО")
        print("-" * 30)

        course_url, weeks_to_process, quality = self.get_course_info()

        if not self.downloader:
            self.downloader = StepikDownloader()

        try:
            self.downloader.download_course_videos(
                course_url=course_url,
                weeks_to_process=weeks_to_process,
                quality=quality
            )
            input("\nНажмите Enter чтобы продолжить...")
        except Exception as e:
            logger.error(f"Ошибка скачивания: {e}")
            input("\nОшибка! Нажмите Enter чтобы вернуться в меню...")

    def transcribe_videos(self):
        """Опция 2: Транскрибация"""
        print("\nТРАНСКРИБАЦИЯ ВИДЕО")
        print("-" * 30)

        model_size, transcribe_weeks = self.get_transcribe_info()

        if not self.transcriber:
            self.transcriber = WhisperTranscriber(model_size=model_size)

        try:
            results = self.transcriber.transcribe_course(
                course_videos_dir="./data/videos",
                weeks_to_process=transcribe_weeks
            )

            # Статистика
            total_files = sum(len(week_results) for week_results in results.values())
            print(f"\nСтатистика транскрибации:")
            print(f"Обработано недель: {len(results)}")
            print(f"Транскрибировано файлов: {total_files}")

            input("\nНажмите Enter чтобы продолжить...")
        except Exception as e:
            logger.error(f"Ошибка транскрибации: {e}")
            input("\nОшибка! Нажмите Enter чтобы вернуться в меню...")

    def full_cycle(self):
        """Опция 3: Полный цикл"""
        print("\nПОЛНЫЙ ЦИКЛ")
        print("-" * 30)

        # Шаг 1: Скачивание
        print("ШАГ 1: Загрузка видео")
        course_url, weeks_to_process, quality = self.get_course_info()

        if not self.downloader:
            self.downloader = StepikDownloader()

        try:
            self.downloader.download_course_videos(
                course_url=course_url,
                weeks_to_process=weeks_to_process,
                quality=quality
            )
        except Exception as e:
            logger.error(f"Ошибка скачивания: {e}")
            input("\nОшибка скачивания! Нажмите Enter чтобы вернуться в меню...")
            return

        # Шаг 2: Транскрибация
        print("\nШАГ 2: Транскрибация")
        transcribe_now = input("Начать транскрибацию сейчас? (y/n): ").strip().lower()

        if transcribe_now == 'y':
            model_size, transcribe_weeks = self.get_transcribe_info()

            if not self.transcriber:
                self.transcriber = WhisperTranscriber(model_size=model_size)

            try:
                results = self.transcriber.transcribe_course(
                    course_videos_dir="./data/videos",
                    weeks_to_process=transcribe_weeks
                )

                # Статистика
                total_files = sum(len(week_results) for week_results in results.values())
                print(f"\nПОЛНЫЙ ЦИКЛ ЗАВЕРШЕН!")
                print(f"Скачано и транскрибировано: {total_files} файлов")

            except Exception as e:
                logger.error(f"Ошибка транскрибации: {e}")
                print("Транскрибация завершена с ошибками")

        input("\nНажмите Enter чтобы вернуться в меню...")

    def run(self):
        """Запуск приложения"""
        logger.info("Запуск Stepik AI Assistant")

        while True:
            self.show_menu()
            choice = input("\nВыберите действие (1-4): ").strip()

            if choice == "1":
                self.download_videos()
            elif choice == "2":
                self.transcribe_videos()
            elif choice == "3":
                self.full_cycle()
            elif choice == "4":
                print("\nДо свидания!")
                break
            else:
                print("\nНеверный выбор! Попробуйте снова.")
                input("Нажмите Enter чтобы продолжить...")


def main():
    try:
        assistant = StepikAIAssistant()
        assistant.run()
    except KeyboardInterrupt:
        print("\n\nПрограмма прервана пользователем")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Критическая ошибка: {e}")
        print(f"\nКритическая ошибка: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
