# src/summarizer/mistral_summarizer.py
import os
import time
import random
import requests
from loguru import logger
from typing import Dict, List, Optional
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class MistralSummarizer:
    def __init__(self):
        """
        Инициализация суммаризатора с Mistral API
        """
        self.api_key = os.getenv('MISTRAL_API_KEY')
        if not self.api_key:
            raise ValueError("MISTRAL_API_KEY должен быть указан в .env файле")

        self.base_url = "https://api.mistral.ai/v1"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        # Обновленный системный промпт в MistralSummarizer
        self.system_prompt = """Ты - опытный преподаватель и эксперт по созданию учебных конспектов.
        Твоя задача - создавать четкие, структурированные и информативные конспекты на основе транскриптов лекций.

        КРИТИЧЕСКИ ВАЖНЫЕ ТРЕБОВАНИЯ:
        1. ТОЧНО сохраняй все определения, формулы, термины и технические понятия без изменений
        2. Выдели основные темы и ключевые концепции
        3. Организуй информацию логически (можно использовать подзаголовки)
        4. Используй маркированные списки для перечислений
        5. Сохрани практические примеры и кейсы
        6. Выдели выводы и основные идеи
        7. Будь лаконичным, но информативным

        ПРАВИЛА ДЛЯ ОПРЕДЕЛЕНИЙ:
        - Определения, формулы, математические выражения сохраняй ДОСЛОВНО
        - Технические термины и специальная лексика остаются без изменений
        - Если в лекции есть точные формулировки определений - копируй их полностью
        - Научные понятия и термины не перефразируй

        ПРАВИЛО ДЛЯ ИЗОБРАЖЕНИЙ:
        - Если лектор ссылается на слайд или изображение, то вставь [СЛАЙД: тема слайда]

        Формат:
        - Заголовок (основная тема)
        - Ключевые определения и термины (дословно)
        - Основные концепции и идеи
        - Практические примеры
        - Выводы

        Для всего остального содержания используй перефразирование и структурирование, но определения сохраняй точно."""

        logger.info("MistralSummarizer инициализирован")

    def make_api_request(self, messages: List[Dict]) -> str:
        """
        Отправка запроса к Mistral API с обработкой лимитов
        """
        max_retries = 3
        base_delay = 10

        for attempt in range(max_retries):
            try:
                data = {
                    "model": "mistral-large-latest",
                    "messages": messages,
                    "temperature": 0.3,
                    "max_tokens": 4000
                }

                response = requests.post(
                    f"{self.base_url}/chat/completions",
                    headers=self.headers,
                    json=data,
                    timeout=60
                )

                if response.status_code == 429:
                    # Лимит запросов - ждем и пробуем снова
                    retry_after = int(response.headers.get('Retry-After', base_delay))
                    wait_time = retry_after + random.randint(1, 5)
                    logger.warning(f"Лимит запросов. Ждем {wait_time} секунд...")
                    time.sleep(wait_time)
                    continue

                response.raise_for_status()

                result = response.json()
                return result["choices"][0]["message"]["content"]

            except requests.exceptions.HTTPError as e:
                if response.status_code == 429 and attempt < max_retries - 1:
                    # Продолжаем повторять для 429 ошибки
                    continue
                logger.error(f"Ошибка Mistral API: {e}")
                raise
            except Exception as e:
                logger.error(f"Ошибка Mistral API: {e}")
                raise

        # Если все попытки исчерпаны
        raise Exception(f"Превышено максимальное количество попыток ({max_retries}) из-за лимита запросов")

    def summarize_transcript(self, transcript_text: str, video_title: str = "") -> Dict:
        """
        Создание конспекта из транскрипта
        """
        logger.info(f"Создание конспекта для: {video_title}")

        user_prompt = f"""
На основе следующего транскрипта лекции создай учебный конспект:

Название/тема: {video_title if video_title else 'Лекция'}

Транскрипт:
{transcript_text}

Создай структурированный конспект, выделяя ключевые моменты."""

        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": user_prompt}
        ]

        try:
            summary = self.make_api_request(messages)

            return {
                "summary": summary,
                "video_title": video_title
            }

        except Exception as e:
            logger.error(f"Ошибка создания конспекта: {e}")
            raise

    def summarize_week_transcripts(self, week_transcripts_dir: str, week_output_dir: str) -> List[Dict]:
        """
        Создание конспектов для всех транскриптов недели с задержками
        """
        if not os.path.exists(week_transcripts_dir):
            raise FileNotFoundError(f"Папка с транскриптами не найдена: {week_transcripts_dir}")

        logger.info(f"Создание конспектов для недели: {week_transcripts_dir}")

        # Ищем файлы транскриптов
        transcript_files = []
        for file in os.listdir(week_transcripts_dir):
            if file.endswith('_transcript.txt') and not file.startswith('.'):
                transcript_files.append(os.path.join(week_transcripts_dir, file))

        if not transcript_files:
            logger.warning(f"В папке {week_transcripts_dir} не найдено файлов транскриптов")
            return []

        logger.info(f"Найдено транскриптов для суммаризации: {len(transcript_files)}")

        results = []
        for i, transcript_file in enumerate(transcript_files):
            try:
                # Добавляем задержку между запросами (кроме первого)
                if i > 0:
                    delay = random.uniform(2, 5)  # Случайная задержка 2-5 секунд
                    logger.info(f"Задержка {delay:.1f} секунд перед следующим запросом...")
                    time.sleep(delay)

                # Читаем транскрипт
                with open(transcript_file, 'r', encoding='utf-8') as f:
                    transcript_text = f.read().strip()

                # Извлекаем название видео из имени файла
                base_name = os.path.basename(transcript_file).replace('_transcript.txt', '')

                # Создаем конспект
                summary_result = self.summarize_transcript(transcript_text, base_name)

                # Сохраняем конспект
                os.makedirs(week_output_dir, exist_ok=True)
                summary_file = os.path.join(week_output_dir, f"{base_name}_summary.txt")

                with open(summary_file, 'w', encoding='utf-8') as f:
                    f.write(summary_result["summary"])

                summary_result["summary_path"] = summary_file
                results.append(summary_result)

                logger.success(f"Конспект создан: {os.path.basename(summary_file)}")

            except Exception as e:
                logger.error(f"Не удалось создать конспект для {transcript_file}: {e}")
                # Если это лимит запросов, прерываем всю обработку
                if "429" in str(e) or "лимит" in str(e).lower():
                    logger.error("Прерывание из-за лимита запросов API")
                    break
                continue

        logger.success(f"Создание конспектов завершено: {len(results)}/{len(transcript_files)}")
        return results

    def summarize_course(self, transcription_dir: str = "./data/transcription",
                         summaries_dir: str = "./data/summaries",
                         weeks_to_process: Optional[List[int]] = None) -> Dict:
        """
        Создание конспектов для всего курса
        """
        if not os.path.exists(transcription_dir):
            raise FileNotFoundError(f"Папка с транскриптами не найдена: {transcription_dir}")

        logger.info(f"Создание конспектов курса: {transcription_dir}")

        # Ищем папки недель
        week_dirs = []
        for item in os.listdir(transcription_dir):
            item_path = os.path.join(transcription_dir, item)
            if os.path.isdir(item_path) and item.startswith("week_"):
                week_dirs.append(item_path)

        week_dirs.sort(key=lambda x: int(x.split("_")[-1]))

        if weeks_to_process:
            week_dirs = [wd for wd in week_dirs if int(wd.split("_")[-1]) in weeks_to_process]

        if not week_dirs:
            logger.warning("Не найдено папок недель для обработки")
            return {}

        logger.info(f"Найдено недель для создания конспектов: {len(week_dirs)}")

        course_results = {}
        for week_dir in week_dirs:
            week_num = int(week_dir.split("_")[-1])
            logger.info(f"Создание конспектов для недели {week_num}")

            # Создаем папку для конспектов недели
            week_output_dir = os.path.join(summaries_dir, f"week_{week_num}")
            try:
                week_results = self.summarize_week_transcripts(week_dir, week_output_dir)
                course_results[week_num] = week_results
            except Exception as e:
                logger.error(f"Ошибка создания конспектов недели {week_num}: {e}")
                course_results[week_num] = []

        total_summaries = sum(len(results) for results in course_results.values())
        logger.success(f"Создание конспектов курса завершено: {total_summaries} конспектов")

        return course_results
