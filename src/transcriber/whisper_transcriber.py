# src/transcriber/whisper_transcriber.py
import os
import whisper
from loguru import logger
from typing import Dict, List, Optional
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class WhisperTranscriber:
    def __init__(self, model_size: str = "medium"):
        """
        Инициализация транскрибатора

        Args:
            model_size: размер модели whisper ("tiny", "base", "small", "medium", "large")
        """
        self.model_size = model_size
        self.model = None
        logger.info(f"WhisperTranscriber инициализирован с моделью: {model_size}")

    def load_model(self):
        """Загрузка модели Whisper (выполняется при первом использовании)"""
        if self.model is None:
            logger.info("Загрузка модели Whisper...")
            self.model = whisper.load_model(self.model_size)
            logger.success("Модель Whisper загружена")

    def transcribe_video(self, video_path: str, output_dir: str) -> Dict:
        """
        Транскрибация видео/аудио файла

        Args:
            video_path: путь к видео файлу
            output_dir: папка для сохранения результата

        Returns:
            Словарь с результатами транскрибации
        """
        self.load_model()

        if not os.path.exists(video_path):
            raise FileNotFoundError(f"Файл не найден: {video_path}")

        logger.info(f"Транскрибация: {os.path.basename(video_path)}")

        try:
            # Транскрибация
            result = self.model.transcribe(
                video_path,
                language="ru",
                verbose=False
            )

            # Сохранение результата
            transcript_text = result["text"].strip()

            os.makedirs(output_dir, exist_ok=True)

            # Формируем имя файла для транскрипта
            base_name = os.path.splitext(os.path.basename(video_path))[0]
            transcript_path = os.path.join(output_dir, f"{base_name}_transcript.txt")

            # Сохраняем текст
            with open(transcript_path, "w", encoding="utf-8") as f:
                f.write(transcript_text)

            # Сохраняем полный результат (сегменты, временные метки)
            transcript_json_path = os.path.join(output_dir, f"{base_name}_transcript.json")
            import json
            with open(transcript_json_path, "w", encoding="utf-8") as f:
                json.dump(result, f, ensure_ascii=False, indent=2)

            logger.success(f"Транскрибация завершена: {os.path.basename(video_path)}")
            logger.info(f"Текст сохранен: {transcript_path}")

            return {
                "text": transcript_text,
                "segments": result.get("segments", []),
                "language": result.get("language", "ru"),
                "transcript_path": transcript_path,
                "json_path": transcript_json_path,
                "video_path": video_path
            }

        except Exception as e:
            logger.error(f"Ошибка транскрибации {video_path}: {e}")
            raise

    def transcribe_week_videos(self, week_videos_dir: str, week_output_dir: str) -> List[Dict]:
        """
        Транскрибация всех видео в папке недели

        Args:
            week_videos_dir: папка с видео недели (например, './data/videos/week_1')
            week_output_dir: папка для сохранения транскриптов недели

        Returns:
            Список результатов транскрибации для каждого видео
        """
        if not os.path.exists(week_videos_dir):
            raise FileNotFoundError(f"Папка недели не найдена: {week_videos_dir}")

        logger.info(f"Транскрибация видео в папке: {week_videos_dir}")

        # Ищем все видео файлы
        video_extensions = ('.mp4', '.avi', '.mov', '.mkv', '.webm')
        video_files = []

        for file in os.listdir(week_videos_dir):
            if file.lower().endswith(video_extensions) and not file.startswith('.'):
                video_files.append(os.path.join(week_videos_dir, file))

        if not video_files:
            logger.warning(f"В папке {week_videos_dir} не найдено видео файлов")
            return []

        logger.info(f"Найдено видео для транскрибации: {len(video_files)}")

        results = []
        for video_path in video_files:
            try:
                result = self.transcribe_video(video_path, week_output_dir)
                results.append(result)
            except Exception as e:
                logger.error(f"Не удалось транскрибировать {video_path}: {e}")
                continue

        logger.success(f"Транскрибация недели завершена: {len(results)}/{len(video_files)} файлов")
        return results

    def transcribe_course(self, course_videos_dir: str = "./data/videos",
                          transcription_dir: str = "./data/transcription",
                          weeks_to_process: Optional[List[int]] = None) -> Dict:
        """
        Транскрибация всего курса

        Args:
            course_videos_dir: корневая папка с видео курса
            transcription_dir: папка для сохранения транскриптов
            weeks_to_process: список номеров недель для обработки (если None - все недели)

        Returns:
            Словарь с результатами по неделям
        """
        if not os.path.exists(course_videos_dir):
            raise FileNotFoundError(f"Папка с видео курса не найдена: {course_videos_dir}")

        logger.info(f"Транскрибация курса: {course_videos_dir}")

        # Ищем папки недель
        week_dirs = []
        for item in os.listdir(course_videos_dir):
            item_path = os.path.join(course_videos_dir, item)
            if os.path.isdir(item_path) and item.startswith("week_"):
                week_dirs.append(item_path)

        week_dirs.sort(key=lambda x: int(x.split("_")[-1]))

        if weeks_to_process:
            week_dirs = [wd for wd in week_dirs if int(wd.split("_")[-1]) in weeks_to_process]

        if not week_dirs:
            logger.warning("Не найдено папок недель для обработки")
            return {}

        logger.info(f"Найдено недель для транскрибации: {len(week_dirs)}")

        course_results = {}
        for week_dir in week_dirs:
            week_num = int(week_dir.split("_")[-1])
            logger.info(f"Транскрибация недели {week_num}")

            # Создаем соответствующую папку для транскриптов недели
            week_output_dir = os.path.join(transcription_dir, f"week_{week_num}")

            try:
                week_results = self.transcribe_week_videos(week_dir, week_output_dir)
                course_results[week_num] = week_results
            except Exception as e:
                logger.error(f"Ошибка транскрибации недели {week_num}: {e}")
                course_results[week_num] = []

        total_transcribed = sum(len(results) for results in course_results.values())
        logger.success(f"Транскрибация курса завершена: {total_transcribed} файлов")

        return course_results
