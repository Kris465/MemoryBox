# main.py
import sys
from dotenv import load_dotenv, find_dotenv
from loguru import logger
from src.downloader.stepik_downloader import StepikDownloader
from src.transcriber.whisper_transcriber import WhisperTranscriber
from src.summarizer.mistral_summarizer import MistralSummarizer
from src.slide_extractor.slide_detector import SlideDetector

# Настройка логов
logger.add("logs/stepik_assistant.log", rotation="10 MB", level="INFO")


class StepikAIAssistant:
    def __init__(self):
        load_dotenv(find_dotenv())
        self.downloader = None
        self.transcriber = None
        self.summarizer = None
        self.slide_extractor = None

    def show_menu(self):
        """Главное меню"""
        print("1. Скачать видео")
        print("2. Транскрибировать видео") 
        print("3. Создать конспекты")
        print("4. Извлечь слайды из видео")
        print("5. Полный цикл (со слайдами)")
        print("6. Выход")

    def get_course_info(self):
        """Получение информации о курсе"""
        course_url = input("Ссылка на курс Stepik: ").strip()
        weeks_input = input("Недель обработать (пусто = все): ").strip()
        weeks_to_process = int(weeks_input) if weeks_input else None
        return course_url, weeks_to_process

    def get_weeks_info(self):
        """Получение информации о неделях для обработки"""
        weeks_input = input("Недели через запятую (пусто = все): ").strip()
        if weeks_input:
            weeks_to_process = [int(w.strip()) for w in weeks_input.split(",")]
        else:
            weeks_to_process = None
        return weeks_to_process

    def download_videos(self, course_url: str, weeks_to_process: int = None):
        """Скачивание видео"""
        if not self.downloader:
            self.downloader = StepikDownloader()
        self.downloader.download_course_videos(
            course_url=course_url,
            weeks_to_process=weeks_to_process,
            quality="720"
        )

    def transcribe_videos(self, weeks_to_process: int = None):
        """Транскрибация видео"""
        if not self.transcriber:
            self.transcriber = WhisperTranscriber(model_size="medium")
        results = self.transcriber.transcribe_course(
            course_videos_dir="./data/videos",
            transcription_dir="./data/transcription",
            weeks_to_process=[weeks_to_process] if weeks_to_process else None
        )
        return sum(len(week_results) for week_results in results.values())

    def create_summaries(self, weeks_to_process: int = None):
        """Создание конспектов"""
        if not self.summarizer:
            self.summarizer = MistralSummarizer()
        results = self.summarizer.summarize_course(
            transcription_dir="./data/transcription",
            summaries_dir="./data/summaries",
            weeks_to_process=[weeks_to_process] if weeks_to_process else None
        )
        return sum(len(week_results) for week_results in results.values())

    def run_download_only(self):
        """Опция 1: Только скачать"""
        print("\n-- Скачивание видео --")
        course_url, weeks_to_process = self.get_course_info()
        try:
            self.download_videos(course_url, weeks_to_process)
            print("Загрузка завершена")
        except Exception as e:
            print(f"Ошибка: {e}")

    def run_transcribe_only(self):
        """Опция 2: Только транскрибировать"""
        print("\n-- Транскрибация --")
        weeks_to_process = self.get_weeks_info()
        try:
            total_files = self.transcribe_videos(weeks_to_process)
            print(f"Транскрибировано: {total_files} файлов")
        except Exception as e:
            print(f"Ошибка: {e}")

    def run_summarize_only(self):
        """Опция 3: Только конспекты"""
        print("\n-- Создание конспектов --")
        weeks_to_process = self.get_weeks_info()
        try:
            total_summaries = self.create_summaries(weeks_to_process)
            print(f"Создано конспектов: {total_summaries}")
        except Exception as e:
            print(f"Ошибка: {e}")

    def run_full_cycle(self):
        """Опция 4: Полный цикл"""
        print("\n-- Полный цикл --")
        course_url, weeks_to_process = self.get_course_info()
        try:
            print("Скачивание...")
            self.download_videos(course_url, weeks_to_process)

            print("Транскрибация...")
            total_files = self.transcribe_videos(weeks_to_process)

            print("Создание конспектов...")
            total_summaries = self.create_summaries(weeks_to_process)

            print(f"Готово! Обработано: {total_files} файлов, создано: {total_summaries} конспектов")
        except Exception as e:
            print(f"Ошибка: {e}")

    def extract_slides(self, weeks_to_process: int = None):
        """Извлечение слайдов"""
        if not self.slide_extractor:
            self.slide_extractor = SlideDetector()
        results = self.slide_extractor.extract_course_slides(
            course_videos_dir="./data/videos",
            slides_dir="./data/slides", 
            weeks_to_process=[weeks_to_process] if weeks_to_process else None
        )
        return sum(len(week_slides) for week_slides in results.values())

    def run_extract_slides_only(self):
        """Опция 5: Только извлечение слайдов"""
        print("\n-- Извлечение слайдов --")
        weeks_to_process = self.get_weeks_info()
        try:
            total_slides = self.extract_slides(weeks_to_process)
            print(f"Извлечено слайдов: {total_slides}")
        except Exception as e:
            print(f"Ошибка: {e}")

    def run_full_cycle_with_slides(self):
        """Опция 5: Полный цикл со слайдами"""
        print("\n-- Полный цикл (со слайдами) --")
        course_url, weeks_to_process = self.get_course_info()
        try:
            print("Скачивание...")
            self.download_videos(course_url, weeks_to_process)

            print("Транскрибация...")
            total_files = self.transcribe_videos(weeks_to_process)

            print("Извлечение слайдов...")
            total_slides = self.extract_slides(weeks_to_process)

            print("Создание конспектов...")
            total_summaries = self.create_summaries(weeks_to_process)

            print(f"Готово! Обработано: {total_files} файлов, извлечено: {total_slides} слайдов, создано: {total_summaries} конспектов")
        except Exception as e:
            print(f"Ошибка: {e}")

    def run(self):
        """Запуск приложения"""
        logger.info("Запуск Stepik AI Assistant")
        while True:
            self.show_menu()
            choice = input("\nВыбор: ").strip()

            if choice == "1":
                self.run_download_only()
            elif choice == "2":
                self.run_transcribe_only()
            elif choice == "3":
                self.run_summarize_only()
            elif choice == "4":
                self.run_extract_slides_only()
            elif choice == "5":
                self.run_full_cycle_with_slides()
            elif choice == "6":
                print("Выход")
                break

            input("\nEnter чтобы продолжить...")


def main():
    try:
        assistant = StepikAIAssistant()
        assistant.run()
    except KeyboardInterrupt:
        print("\nПрервано пользователем")
        sys.exit(0)
    except Exception as e:
        print(f"Ошибка: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
