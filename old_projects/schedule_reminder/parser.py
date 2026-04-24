import os
from datetime import date, datetime
from typing import Dict, List
from dotenv import load_dotenv, find_dotenv
from playwright.async_api import async_playwright
from loguru import logger

from json_tools import ScheduleJsonTools

load_dotenv(find_dotenv())


class UniversityParser:
    """Парсер расписания университета"""

    def __init__(self, headless: bool = True, use_saved_session: bool = True):
        self.headless = headless
        self.use_saved_session = use_saved_session  # Whether to try using saved session
        self.login = os.getenv('LOGIN')
        self.password = os.getenv('PASSWORD')
        self.group_id = os.getenv('GROUP_UNIVERSITY_ID', '12054')  # Default to 12054 for backward compatibility
        self.json_tools = ScheduleJsonTools()

        if not self.login or not self.password:
            raise ValueError("Логин или пароль не найдены в .env файле")

    def is_calendar_data_current(self) -> bool:
        """Проверяет, содержит ли файл с расписанием актуальные данные на сегодня"""
        try:
            events = self.json_tools.load_events_from_json()
            if not events:
                logger.info("Нет сохраненных данных расписания")
                return False

            # Получаем сегодняшнюю дату
            today = date.today()

            # Находим минимальную и максимальную даты в расписании
            event_dates = []
            for event in events:
                date_str = event.get('date')
                if date_str:
                    try:
                        event_date = datetime.strptime(date_str, '%Y-%m-%d').date()
                        event_dates.append(event_date)
                    except ValueError:
                        continue

            if not event_dates:
                logger.warning("Не найдены корректные даты в расписании")
                return False

            min_date = min(event_dates)
            max_date = max(event_dates)

            logger.info(f"Диапазон дат в расписании: {min_date} - {max_date}")
            logger.info(f"Сегодня: {today}")

            # Проверяем, находится ли сегодняшняя дата в диапазоне
            is_current = min_date <= today <= max_date

            if not is_current:
                logger.info("Расписание не содержит актуальные данные для сегодня. Нужно обновить.")
            else:
                logger.info("Расписание содержит актуальные данные для сегодня.")

            return is_current

        except Exception as e:
            logger.error(f"Ошибка при проверке актуальности расписания: {e}")
            return False

    async def parse_and_save_schedule(self, force_update=False) -> bool:
        """Основная функция: парсит расписание и сохраняет в JSON"""
        try:
            # Проверяем, нужно ли обновлять расписание
            if not force_update and self.is_calendar_data_current():
                logger.info("Расписание содержит актуальные данные, обновление не требуется")
                return True

            logger.info("Начинаем парсинг расписания...")

            events_data = await self._parse_calendar_data()
            if events_data:
                return self.json_tools.save_events_to_json(events_data)
            return False

        except Exception as e:
            logger.error(f"Ошибка при парсинге расписания: {e}")
            return False

    async def _parse_calendar_data(self) -> List[Dict]:
        """Парсит данные календаря с сайта"""
        async with async_playwright() as playwright:
            browser = await playwright.chromium.launch(headless=self.headless)

            context_args = {
                'viewport': {'width': 1280, 'height': 800},
                'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }

            # Используем сохраненную сессию если доступна
            if self.use_saved_session and os.path.exists("auth_state.json"):
                context = await browser.new_context(
                    **context_args, storage_state="auth_state.json")
                logger.info("Используем сохраненную сессию")
            else:
                context = await browser.new_context(**context_args)

            page = await context.new_page()

            try:
                # Логинимся если нужно
                if not await self._ensure_login(page):
                    logger.error("Не удалось авторизоваться")
                    return []

                # Переходим к календарю
                calendar_url = f'https://es.unitech-mo.ru/WebApp/#/RaspCalendar/Group/{self.group_id}'
                await page.goto(calendar_url, wait_until='networkidle')
                await page.wait_for_timeout(5000)
                await page.wait_for_selector('.v-event', timeout=10000)

                # Пытаемся навигироваться к текущей дате, если есть такая возможность
                try:
                    # Ищем кнопку "Сегодня" или аналогичную для навигации к текущей дате
                    today_button = page.locator('button:has-text("Сегодня"), button:has-text("Today"), .today-button, [data-today]')
                    if await today_button.count() > 0:
                        await today_button.click()
                        await page.wait_for_timeout(2000)  # Ждем загрузки
                    else:
                        # Если кнопки "Сегодня" нет, пробуем использовать календарь для навигации
                        # Ищем элементы навигации по датам
                        await page.wait_for_timeout(1000)
                except Exception as nav_error:
                    logger.warning(f"Не удалось навигироваться к текущей дате: {nav_error}")
                    # Продолжаем с текущим отображением календаря

                # Парсим все события
                events = await page.locator('.v-event').all()
                logger.info(f"Найдено событий: {len(events)}")

                events_data = []

                for event in events:
                    try:
                        event_date = await event.get_attribute('data-date')
                        event_text = await event.text_content()
                        event_lines = [line.strip() for line in event_text.split('\n') if line.strip()]

                        background_color = await event.evaluate('(element) => getComputedStyle(element).backgroundColor')
                        # Парсим детали занятия
                        parsed_event = self._parse_event_details(event_date, event_lines, background_color)
                        events_data.append(parsed_event)

                    except Exception as e:
                        logger.warning(f"Ошибка парсинга события: {e}")
                        continue

                # Проверяем, нужно ли сохранять сессию.
                # Университетские куки протухают ежедневно, просто удаляем старую сессию чтобы не накапливались
                try:
                    if os.path.exists("auth_state.json"):
                        os.remove("auth_state.json")
                except Exception as e:
                    logger.warning(f"Ошибка при удалении файла сессии auth_state.json: {e}")

                return events_data

            finally:
                await browser.close()

    async def _ensure_login(self, page) -> bool:
        """Обеспечивает авторизацию на сайте"""
        try:
            # Проверяем текущий URL, чтобы понять, нужна ли авторизация
            current_url = page.url
            if 'login' not in current_url.lower():
                # Проверяем, можем ли мы получить доступ к календарю
                calendar_url = f'https://es.unitech-mo.ru/WebApp/#/RaspCalendar/Group/{self.group_id}'
                await page.goto(calendar_url, wait_until='networkidle')

                # Если нас перенаправило на login, значит сессия протухла
                if 'login' in page.url.lower():
                    logger.info("Сессия протухла, требуется повторная авторизация")
                else:
                    # Если мы остались на нужной странице, возможно сессия еще действует
                    return True

            # Переходим на страницу логина
            await page.goto('https://es.unitech-mo.ru/WebApp/#/login',
                            wait_until='networkidle')
            await page.wait_for_timeout(3000)

            # Логинимся
            inputs = await page.query_selector_all('input')
            if len(inputs) >= 2:
                await inputs[0].fill(self.login)
                await inputs[1].fill(self.password)
                await inputs[1].press('Enter')
                await page.wait_for_timeout(5000)

            # Проверяем, успешно ли вошли
            return 'login' not in page.url.lower()

        except Exception as e:
            logger.error(f"Ошибка при авторизации: {e}")
            return False

    def _parse_event_details(self, date: str, lines: List[str], color: str) -> Dict:
        """Парсит детали одного занятия"""
        import re

        # Возвращаем только необходимые поля для упрощенной структуры
        event_data = {
            'date': date,
            'time': '',
            'type': '',
            'subject': '',
            'room': '',
            'teacher': '',
            'original_text': ' | '.join(lines)  # Сохраняем оригинальный текст на всякий случай
        }

        try:
            if lines:
                full_text = lines[0]

                # Используем регулярные выражения для извлечения данных, учитывая два возможных формата:
                # 1. Обычный формат: "20:35 пр Основы теории информационной безопасности 2112 20:35 - 22:00 2112, пр. Вихров А.П.Гр. БМЗ-25"
                # 2. Формат дистанционки: "09:00 пр Специальные разделы математики  09:00 - 10:30 Дистанционно, пр. Скрипкина Е.В.Гр. БМЗ-25"

                # Сначала пробуем формат с аудиторией
                pattern_with_room = r'(\d{1,2}:\d{2})\s+(лек|пр|лаб|сем|прак|зач|экз|конс)\s+([^.]+?)\s+(\d+[а-яА-Я]?)\s+\d{1,2}:\d{2}\s*[-–]\s*\d{1,2}:\d{2}\s+\d+[а-яА-Я]?\s*,\s*пр\.\s*([^,]+?)(?:,|Гр\.|группа)'
                match = re.search(pattern_with_room, full_text)

                if match:
                    event_data['time'] = match.group(1)  # 20:35
                    event_data['type'] = match.group(2)  # пр
                    event_data['subject'] = match.group(3).strip()  # Основы теории информационной безопасности
                    event_data['room'] = f"ауд. {match.group(4)}"  # 2112 (с добавлением "ауд.")
                    event_data['teacher'] = match.group(5).strip()  # Вихров А.П.
                else:
                    # Пробуем формат с дистанционным обучением
                    pattern_remote = r'(\d{1,2}:\d{2})\s+(лек|пр|лаб|сем|прак|зач|экз|конс)\s+([^.]+?)\s+\d{1,2}:\d{2}\s*[-–]\s*\d{1,2}:\d{2}\s+(Дистанционно),\s*пр\.\s*([^,]+?)(?:,|Гр\.|группа)'
                    match = re.search(pattern_remote, full_text)

                    if match:
                        event_data['time'] = match.group(1)  # 09:00
                        event_data['type'] = match.group(2)  # пр
                        event_data['subject'] = match.group(3).strip()  # Специальные разделы математики
                        event_data['room'] = match.group(4)  # Дистанционно
                        event_data['teacher'] = match.group(5).strip()  # Скрипкина Е.В.
                    else:
                        # Резервный вариант на случай непредвиденного формата
                        # Извлекаем только время и тип, остальное оставляем пустым
                        time_match = re.search(r'(\d{1,2}:\d{2})', full_text)
                        if time_match:
                            event_data['time'] = time_match.group(1)

                        type_match = re.search(r'\s+(лек|пр|лаб|сем|прак|зач|экз|конс)\s+', full_text)
                        if type_match:
                            event_data['type'] = type_match.group(1)

        except Exception as e:
            logger.warning(f"Ошибка детального парсинга события: {e}")

        return event_data


async def update_schedule_daily():
    """Функция для ежедневного обновления расписания"""
    parser = UniversityParser(headless=True, use_saved_session=True)
    # Обновляем расписание, позволяя логике проверить актуальность
    success = await parser.parse_and_save_schedule()
    return success
