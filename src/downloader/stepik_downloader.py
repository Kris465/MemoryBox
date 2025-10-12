import json
import os
import urllib.request
import requests
import sys
from typing import List, Dict, Optional
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv, find_dotenv
from loguru import logger
from src.utils.url_parser import extract_course_id


load_dotenv(find_dotenv())


class StepikDownloader:
    def __init__(self):
        """Инициализация с загрузкой credentials из .env"""
        self.client_id = os.getenv('STEPIK_CLIENT_ID')
        self.client_secret = os.getenv('STEPIK_CLIENT_SECRET')

        if not self.client_id or not self.client_secret:
            raise ValueError("STEPIK_CLIENT_ID и STEPIK_CLIENT_SECRET должны быть указаны в .env файле")

        self.token = self._get_token()
        logger.info("StepikDownloader инициализирован")

    def _get_token(self) -> str:
        """Получение OAuth токена для доступа к Stepik API"""
        try:
            auth = HTTPBasicAuth(self.client_id, self.client_secret)
            resp = requests.post(
                'https://stepik.org/oauth2/token/', 
                data={'grant_type': 'client_credentials'}, 
                auth=auth
            )
            resp.raise_for_status()
            token = json.loads(resp.text)['access_token']
            logger.success("Токен успешно получен")
            return token
        except Exception as e:
            logger.error(f"Ошибка получения токена: {e}")
            raise

    def _make_api_request(self, url: str) -> Dict:
        """Универсальный метод для API запросов"""
        try:
            response = requests.get(url, headers={'Authorization': 'Bearer ' + self.token})
            response.raise_for_status()
            return json.loads(response.text)
        except Exception as e:
            logger.error(f"Ошибка API запроса {url}: {e}")
            raise

    def get_course_structure(self, course_id: str) -> Dict:
        """Получение структуры курса"""
        logger.info(f"Получение структуры курса {course_id}")
        return self._make_api_request(f'https://stepik.org/api/courses/{course_id}')

    def get_all_sections(self, course_data: Dict) -> List[int]:
        """Получение списка разделов (недель) курса"""
        sections = course_data['courses'][0]['sections']
        logger.info(f"Найдено разделов: {len(sections)}")
        return sections

    def get_units_for_sections(self, section_ids: List[int]) -> List[List[int]]:
        """Получение юнитов для каждого раздела"""
        logger.info(f"Получение юнитов для {len(section_ids)} разделов")
        units = []
        for section_id in section_ids:
            section_data = self._make_api_request(f'https://stepik.org/api/sections/{section_id}')
            units.append(section_data['sections'][0]['units'])
        return units

    def get_steps_for_week(self, units_list: List[List[int]], week: int) -> List[int]:
        """Получение всех шагов для указанной недели"""
        logger.info(f"Получение шагов для недели {week}")

        # week - 1 потому что недели в коде с 1, а в списке с 0
        unit_ids = units_list[week - 1]

        # Получаем данные по каждому юниту
        units_data = []
        for unit_id in unit_ids:
            unit_data = self._make_api_request(f'https://stepik.org/api/units/{unit_id}')
            units_data.append(unit_data)

        # Извлекаем ID уроков
        lesson_ids = [unit['units'][0]['lesson'] for unit in units_data]

        # Получаем шаги для каждого урока
        all_steps = []
        for lesson_id in lesson_ids:
            lesson_data = self._make_api_request(f'https://stepik.org/api/lessons/{lesson_id}')
            steps = lesson_data['lessons'][0]['steps']
            all_steps.extend(steps)

        logger.info(f"Найдено шагов для недели {week}: {len(all_steps)}")
        return all_steps

    def filter_video_steps(self, step_ids: List[int]) -> List[Dict]:
        """Фильтрация видео и аудио шагов"""
        logger.info(f"Фильтрация медиа из {len(step_ids)} шагов")
        media_blocks = []

        for step_id in step_ids:
            step_data = self._make_api_request(f'https://stepik.org/api/steps/{step_id}')
            step_block = step_data['steps'][0]['block']

            # Проверяем, есть ли видео ИЛИ аудио в шаге
            if step_block.get('video') or step_block.get('audio'):
                media_blocks.append(step_block)

        logger.success(f"Найдено медиа: {len(media_blocks)}")
        return media_blocks

    def get_media_urls(self, media_blocks: List[Dict], quality: str = '720') -> List[Dict]:
        """Получение URL видео и аудио"""
        media_urls = []

        for media_block in media_blocks:
            selected_url = None
            message = None
            media_type = None

            # Обрабатываем видео
            if media_block.get('video'):
                media_type = 'video'
                video_data = media_block['video']

                # Ищем URL с нужным качеством
                for url_info in video_data['urls']:
                    if url_info['quality'] == quality:
                        selected_url = url_info['url']
                        break

                # Если нужное качество не найдено, берем первое доступное
                if not selected_url:
                    selected_url = video_data['urls'][0]['url']
                    message = f"Качество {quality}p недоступно, используется {video_data['urls'][0]['quality']}p"
                    logger.warning(message)

            # Обрабатываем аудио
            elif media_block.get('audio'):
                media_type = 'audio'
                audio_data = media_block['audio']
                selected_url = audio_data['url']  # У аудио обычно один URL

            if selected_url:
                media_urls.append({
                    'url': selected_url,
                    'message': message,
                    'media_type': media_type,  # 'video' или 'audio'
                    'original_block': media_block
                })

        return media_urls

    def _reporthook(self, blocknum, blocksize, totalsize):
        """Прогресс-бар для скачивания"""
        readsofar = blocknum * blocksize
        if totalsize > 0:
            percent = readsofar * 1e2 / totalsize
            s = f"\r{percent:5.1f}% {readsofar:{len(str(totalsize))}d} / {totalsize}"
            sys.stderr.write(s)
            if readsofar >= totalsize:
                sys.stderr.write("\n")
        else:
            sys.stderr.write(f"read {readsofar}\n")

    def download_media(self, media_urls: List[Dict],
                       output_dir: str, week: int):
        """Скачивание видео и аудио файлов"""
        week_dir = os.path.join(output_dir, f'week_{week}')
        os.makedirs(week_dir, exist_ok=True)

        logger.info(f'Скачивание в папку: {week_dir}')

        for i, media_info in enumerate(media_urls):
            # Определяем расширение файла по типу медиа
            extension = '.mp4' if media_info['media_type'] == 'video' else '.mp3'
            filename = os.path.join(week_dir, f'media_{i+1}{extension}')

            # Пропускаем если файл уже существует
            if os.path.isfile(filename):
                logger.info(f'Файл уже существует: {filename}')
                continue

            # Выводим предупреждение о качестве
            if media_info['message']:
                logger.warning(media_info['message'])

            try:
                logger.info(f'Скачивание {media_info["media_type"]}: {filename}')
                urllib.request.urlretrieve(media_info['url'],
                                           filename, self._reporthook)
                logger.success(f'Завершено: {filename}')
            except Exception as e:
                logger.error(f'Ошибка при скачивании {filename}: {e}')
                if os.path.isfile(filename):
                    os.remove(filename)

    def download_course_media(self, course_url: str,
                              weeks_to_process: Optional[int] = None,
                              quality: str = '720',
                              output_dir: str = './data/videos'):
        """Основной метод для скачивания медиа курса"""

        logger.info(f"Начало скачивания курса: {course_url}")

        # Извлекаем ID курса
        course_id = extract_course_id(course_url)
        if not course_id:
            raise ValueError("Не удалось извлечь ID курса из URL")

        # Получаем структуру курса
        course_data = self.get_course_structure(course_id)
        section_ids = self.get_all_sections(course_data)
        all_units = self.get_units_for_sections(section_ids)

        # Определяем сколько недель обрабатывать
        total_weeks = len(section_ids)
        weeks_to_process = weeks_to_process or total_weeks
        weeks_to_process = min(weeks_to_process, total_weeks)

        logger.info(f"Всего недель в курсе: {total_weeks}, будет обработано: {weeks_to_process}")

        # Обрабатываем каждую неделю
        for week in range(1, weeks_to_process + 1):
            logger.info(f"Обработка недели {week}")

            # Получаем медиа для недели
            steps = self.get_steps_for_week(all_units, week)
            media_blocks = self.filter_video_steps(steps)

            if not media_blocks:
                logger.info(f"На неделе {week} нет медиа")
                continue

            media_urls = self.get_media_urls(media_blocks, quality)

            # Скачиваем медиа
            self.download_media(media_urls, output_dir, week)

        logger.success("Скачивание завершено!")
