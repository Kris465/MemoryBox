# src/slide_extractor/slide_detector.py
import cv2
import numpy as np
import os
from pathlib import Path
from loguru import logger
from typing import List, Dict, Optional


class SlideDetector:
    def __init__(self, change_threshold: float = 0.3, min_interval: int = 2):
        """
        Инициализация детектора слайдов

        Args:
            change_threshold: порог изменения между кадрами (0-1)
            min_interval: минимальный интервал между проверками (секунды)
        """
        self.change_threshold = change_threshold
        self.min_interval = min_interval
        logger.info(f"SlideDetector инициализирован (threshold: {change_threshold})")

    def extract_slides_from_video(self, video_path: str,
                                  output_dir: str) -> List[Dict]:
        """
        Извлечение слайдов из одного видео

        Args:
            video_path: путь к видео файлу
            output_dir: папка для сохранения слайдов

        Returns:
            Список информации о сохраненных слайдах
        """
        if not os.path.exists(video_path):
            raise FileNotFoundError(f"Видео не найдено: {video_path}")

        os.makedirs(output_dir, exist_ok=True)

        cap = cv2.VideoCapture(video_path)
        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_interval = int(fps * self.min_interval)

        prev_frame = None
        slides = []
        frame_count = 0
        slide_count = 0

        video_name = Path(video_path).stem
        logger.info(f"Извлечение слайдов из: {video_name}")

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Проверяем кадры с интервалом
            if frame_count % frame_interval == 0:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                if prev_frame is not None:
                    if self._is_slide_change(prev_frame, gray):
                        slide_info = self._save_slide(frame, output_dir, video_name, slide_count, frame_count, fps)
                        slides.append(slide_info)
                        slide_count += 1
                        logger.info(f"Обнаружен слайд #{slide_count} на {slide_info['timestamp']}")

                prev_frame = gray

            frame_count += 1

        cap.release()
        logger.success(f"Извлечено слайдов: {len(slides)} из {video_name}")
        return slides

    def _is_slide_change(self, frame1: np.ndarray, frame2: np.ndarray) -> bool:
        """Определяет, является ли изменение между кадрами сменой слайда"""
        # Разность кадров
        diff = cv2.absdiff(frame1, frame2)
        change_score = np.mean(diff) / 255

        # Дополнительная проверка на гистограммы
        hist1 = cv2.calcHist([frame1], [0], None, [64], [0, 256])
        hist2 = cv2.calcHist([frame2], [0], None, [64], [0, 256])
        hist_diff = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)

        return change_score > self.change_threshold and hist_diff < 0.8

    def _save_slide(self, frame: np.ndarray, output_dir: str, video_name: str,
                    slide_num: int, frame_count: int, fps: float) -> Dict:
        """Сохраняет слайд и возвращает информацию о нем"""
        timestamp = frame_count / fps
        minutes = int(timestamp // 60)
        seconds = int(timestamp % 60)

        filename = f"{video_name}_slide_{slide_num+1:03d}_{minutes:02d}m{seconds:02d}s.jpg"
        filepath = os.path.join(output_dir, filename)

        # Сохраняем в хорошем качестве
        cv2.imwrite(filepath, frame, [cv2.IMWRITE_JPEG_QUALITY, 90])

        return {
            "path": filepath,
            "slide_number": slide_num + 1,
            "timestamp": f"{minutes:02d}:{seconds:02d}",
            "frame": frame_count
        }

    def extract_week_slides(self, week_videos_dir: str, week_output_dir: str) -> List[Dict]:
        """
        Извлечение слайдов из всех видео недели
        """
        if not os.path.exists(week_videos_dir):
            raise FileNotFoundError(f"Папка недели не найдена: {week_videos_dir}")

        logger.info(f"Извлечение слайдов из папки: {week_videos_dir}")

        video_extensions = ('.mp4', '.avi', '.mov', '.mkv', '.webm')
        video_files = []

        for file in os.listdir(week_videos_dir):
            if file.lower().endswith(video_extensions) and not file.startswith('.'):
                video_files.append(os.path.join(week_videos_dir, file))

        if not video_files:
            logger.warning(f"В папке {week_videos_dir} не найдено видео файлов")
            return []

        logger.info(f"Найдено видео для обработки: {len(video_files)}")

        all_slides = []
        for video_path in video_files:
            try:
                video_slides = self.extract_slides_from_video(video_path, week_output_dir)
                all_slides.extend(video_slides)
            except Exception as e:
                logger.error(f"Не удалось обработать {video_path}: {e}")
                continue

        logger.success(f"Извлечение слайдов завершено: {len(all_slides)} слайдов")
        return all_slides

    def extract_course_slides(self, course_videos_dir: str = "./data/videos",
                              slides_dir: str = "./data/slides",
                              weeks_to_process: Optional[List[int]] = None) -> Dict:
        """
        Извлечение слайдов для всего курса
        """
        if not os.path.exists(course_videos_dir):
            raise FileNotFoundError(f"Папка с видео курса не найдена: {course_videos_dir}")

        logger.info(f"Извлечение слайдов курса: {course_videos_dir}")

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

        logger.info(f"Найдено недель для извлечения слайдов: {len(week_dirs)}")

        course_results = {}
        for week_dir in week_dirs:
            week_num = int(week_dir.split("_")[-1])
            logger.info(f"Извлечение слайдов для недели {week_num}")

            # Создаем папку для слайдов недели
            week_output_dir = os.path.join(slides_dir, f"week_{week_num}")

            try:
                week_slides = self.extract_week_slides(week_dir, week_output_dir)
                course_results[week_num] = week_slides
            except Exception as e:
                logger.error(f"Ошибка извлечения слайдов недели {week_num}: {e}")
                course_results[week_num] = []

        total_slides = sum(len(slides) for slides in course_results.values())
        logger.success(f"Извлечение слайдов курса завершено: {total_slides} слайдов")

        return course_results
