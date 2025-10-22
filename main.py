# main.py
import sys
import os
from pathlib import Path
from dotenv import load_dotenv, find_dotenv
from loguru import logger

# Настройка логов
logger.add("logs/stepik_assistant.log", rotation="10 MB", level="INFO")


class StepikAIAssistant:
    def __init__(self):
        load_dotenv(find_dotenv())
        # Инициализация только при необходимости (ленивая загрузка)
        self.downloader = None
        self.transcriber = None
        self.summarizer = None
        self.slide_extractor = None
        self.exporter = None

    def show_menu(self):
        """Главное меню"""
        print("Stepik AI Assistant - Конспект-генератор")
        print("1. Скачать видео с Stepik")
        print("2. Транскрибировать видео") 
        print("3. Создать конспекты")
        print("4. Извлечь слайды из видео")
        print("5. Создать отчеты DOCX")
        print("6. Полный цикл (все этапы)")
        print("7. Выход")

    def _lazy_init_downloader(self):
        """Ленивая инициализация загрузчика"""
        if self.downloader is None:
            from src.downloader.stepik_downloader import StepikDownloader
            self.downloader = StepikDownloader()
        return self.downloader

    def _lazy_init_transcriber(self):
        """Ленивая инициализация транскрибатора"""
        if self.transcriber is None:
            from src.transcriber.whisper_transcriber import WhisperTranscriber
            self.transcriber = WhisperTranscriber(model_size="medium")
        return self.transcriber

    def _lazy_init_summarizer(self):
        """Ленивая инициализация суммаризатора"""
        if self.summarizer is None:
            from src.summarizer.mistral_summarizer import MistralSummarizer
            self.summarizer = MistralSummarizer()
        return self.summarizer

    def _lazy_init_slide_extractor(self):
        """Ленивая инициализация экстрактора слайдов"""
        if self.slide_extractor is None:
            from src.slide_extractor.slide_detector import SlideDetector
            self.slide_extractor = SlideDetector()
        return self.slide_extractor

    def _lazy_init_exporter(self):
        """Ленивая инициализация экспортера"""
        if self.exporter is None:
            from src.exporter.docx_exporter import DocxExporter
            self.exporter = DocxExporter()
        return self.exporter

    def get_course_source(self):
        """Получение информации об источнике курса"""
        print("\n-- Источник видео --")
        print("1. Скачать с Stepik (укажите ссылку)")
        print("2. Использовать локальные видео (уже в папке ./data/videos)")

        choice = input("Выбор (1/2): ").strip()

        if choice == "1":
            course_url = input("Ссылка на курс Stepik: ").strip()
            weeks_input = input("Недель обработать (пусто = все): ").strip()
            weeks_to_process = int(weeks_input) if weeks_input else None
            return {"type": "stepik", "url": course_url, "weeks": weeks_to_process}
        else:
            print("Используются локальные видео из ./data/videos")
            weeks_input = input("Недели через запятую (пусто = все): ").strip()
            if weeks_input:
                weeks_to_process = [int(w.strip()) for w in weeks_input.split(",")]
            else:
                weeks_to_process = None
            return {"type": "local", "weeks": weeks_to_process}

    def get_weeks_info(self, operation_name: str = "обработки"):
        """Получение информации о неделях для обработки"""
        print(f"\n-- {operation_name} --")
        weeks_input = input("Недели через запятую (пусто = все): ").strip()
        if weeks_input:
            try:
                weeks_to_process = [int(w.strip()) for w in weeks_input.split(",")]
                return weeks_to_process
            except ValueError:
                print("Ошибка: введите числа через запятую")
                return self.get_weeks_info(operation_name)
        else:
            return None

    def download_videos(self, course_url: str, weeks_to_process: int = None):
        """Скачивание видео с Stepik"""
        downloader = self._lazy_init_downloader()
        downloader.download_course_videos(
            course_url=course_url,
            weeks_to_process=weeks_to_process,
            quality="720"
        )

    def transcribe_videos(self, weeks_to_process: list = None):
        """Транскрибация видео"""
        transcriber = self._lazy_init_transcriber()
        results = transcriber.transcribe_course(
            course_videos_dir="./data/videos",
            transcription_dir="./data/transcription",
            weeks_to_process=weeks_to_process
        )
        return sum(len(week_results) for week_results in results.values())

    def create_summaries(self, weeks_to_process: list = None):
        """Создание конспектов"""
        summarizer = self._lazy_init_summarizer()
        results = summarizer.summarize_course(
            transcription_dir="./data/transcription",
            summaries_dir="./data/summaries",
            weeks_to_process=weeks_to_process
        )
        return sum(len(week_results) for week_results in results.values())

    def extract_slides(self, weeks_to_process: list = None):
        """Извлечение слайдов"""
        slide_extractor = self._lazy_init_slide_extractor()
        results = slide_extractor.extract_course_slides(
            course_videos_dir="./data/videos",
            slides_dir="./data/slides",
            weeks_to_process=weeks_to_process
        )
        return sum(len(week_slides) for week_slides in results.values())

    def create_reports(self, weeks_to_process: list = None):
        """Создание отчетов в DOCX"""
        exporter = self._lazy_init_exporter()
        results = exporter.export_course_reports(
            summaries_dir="./data/summaries",
            output_dir="./data/reports",
            weeks_to_process=weeks_to_process
        )
        return sum(1 for result in results.values() if result)

    # Опции меню
    def run_download_only(self):
        """Опция 1: Скачать видео"""
        print("\n-- Скачивание видео --")
        try:
            source_info = self.get_course_source()
            if source_info["type"] == "stepik":
                self.download_videos(source_info["url"], source_info["weeks"])
                print("Загрузка завершена")
            else:
                print("Используются локальные видео")
        except Exception as e:
            print(f"Ошибка: {e}")

    def run_transcribe_only(self):
        """Опция 2: Транскрибировать видео"""
        print("\n-- Транскрибация --")
        try:
            weeks_to_process = self.get_weeks_info("транскрибации")
            total_files = self.transcribe_videos(weeks_to_process)
            print(f"Транскрибировано: {total_files} файлов")
        except Exception as e:
            print(f"Ошибка: {e}")

    def run_summarize_only(self):
        """Опция 3: Создать конспекты"""
        print("\n-- Создание конспектов --")
        try:
            weeks_to_process = self.get_weeks_info("создания конспектов")
            total_summaries = self.create_summaries(weeks_to_process)
            print(f"Создано конспектов: {total_summaries}")
        except Exception as e:
            print(f"Ошибка: {e}")

    def run_extract_slides_only(self):
        """Опция 4: Извлечь слайды"""
        print("\n-- Извлечение слайдов --")
        try:
            weeks_to_process = self.get_weeks_info("извлечения слайдов")
            total_slides = self.extract_slides(weeks_to_process)
            print(f"Извлечено слайдов: {total_slides}")
        except Exception as e:
            print(f"Ошибка: {e}")

    def run_create_reports(self):
        """Опция 5: Создать отчеты"""
        print("\n-- Создание отчетов DOCX --")
        print("Тема курса будет определена автоматически из конспектов")
        try:
            weeks_to_process = self.get_weeks_info("создания отчетов")
            total_reports = self.create_reports(weeks_to_process)
            print(f"Создано отчетов: {total_reports}")
        except Exception as e:
            print(f"Ошибка: {e}")

    def run_full_cycle(self):
        """Опция 6: Полный цикл"""
        print("\n-- Полный цикл обработки --")
        try:
            # Шаг 1: Получение источника видео
            source_info = self.get_course_source()
            weeks_to_process = source_info["weeks"]
            
            # Шаг 2: Скачивание (если нужно)
            if source_info["type"] == "stepik":
                print("Скачивание видео...")
                self.download_videos(source_info["url"], weeks_to_process)
            else:
                print("Используются локальные видео")
            
            # Шаг 3: Извлечение слайдов (обязательный этап)
            print("Извлечение слайдов...")
            total_slides = self.extract_slides(weeks_to_process)
            
            # Шаг 4: Транскрибация
            print("Транскрибация...")
            total_files = self.transcribe_videos(weeks_to_process)
            
            # Шаг 5: Создание конспектов
            print("Создание конспектов...")
            total_summaries = self.create_summaries(weeks_to_process)
            
            # Шаг 6: Создание отчетов
            print("Создание отчетов...")
            total_reports = self.create_reports(weeks_to_process)
            
            print("\nПолный цикл завершен!")
            print(f" Видео: {'скачаны' if source_info['type'] == 'stepik' else 'локальные'}")
            print(f"Слайдов: {total_slides}")
            print(f"Транскрибировано: {total_files} файлов")
            print(f"Конспектов: {total_summaries}")
            print(f"Отчетов: {total_reports}")
            
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
                self.run_create_reports()
            elif choice == "6":
                self.run_full_cycle()
            elif choice == "7":
                print("Выход")
                break
            else:
                print("Неверный выбор")

            input("\n↵ Enter чтобы продолжить...")


def main():
    try:
        assistant = StepikAIAssistant()
        assistant.run()
    except KeyboardInterrupt:
        print("\nПрервано пользователем")
        sys.exit(0)
    except Exception as e:
        print(f"Критическая ошибка: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
