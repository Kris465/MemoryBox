import os
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
        self.use_saved_session = use_saved_session
        self.login = os.getenv('LOGIN')
        self.password = os.getenv('PASSWORD')
        self.json_tools = ScheduleJsonTools()

        if not self.login or not self.password:
            raise ValueError("Логин или пароль не найдены в .env файле")

    async def parse_and_save_schedule(self) -> bool:
        """Основная функция: парсит расписание и сохраняет в JSON"""
        try:
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
                context = await browser.new_context(**context_args, storage_state="auth_state.json")
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
                await page.goto('https://es.unitech-mo.ru/WebApp/#/RaspCalendar/Group/12054', wait_until='networkidle')
                await page.wait_for_timeout(5000)
                await page.wait_for_selector('.v-event', timeout=10000)

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

                # Сохраняем сессию для будущего использования
                await context.storage_state(path="auth_state.json")

                return events_data

            finally:
                await browser.close()

    async def _ensure_login(self, page) -> bool:
        """Обеспечивает авторизацию на сайте"""
        try:
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

            return 'login' not in page.url.lower()

        except Exception as e:
            logger.error(f"Ошибка при авторизации: {e}")
            return False

    def _parse_event_details(self, date: str, lines: List[str], color: str) -> Dict:
        """Парсит детали одного занятия"""
        event_data = {
            'date': date,
            'text': ' | '.join(lines),
            'lines': lines,
            'color': color,
            'parsed': {}
        }

        try:
            if lines:
                first_line = lines[0]
                parts = first_line.split(' ')

                if len(parts) >= 2:
                    event_data['parsed']['time'] = parts[0]
                    event_data['parsed']['type'] = parts[1]

                    # Ищем предмет
                    subject_candidates = [line for line in lines if len(line) > 10 and not any(word in line.lower() for word in ['гр.', 'ауд.', 'преподаватель', 'аудитория'])]
                    if subject_candidates:
                        event_data['parsed']['subject'] = subject_candidates[0]

                    # Ищем аудиторию
                    room_candidates = [line for line in lines if any(word in line.lower() for word in ['ауд.', 'аудитория'])]
                    if room_candidates:
                        event_data['parsed']['room'] = room_candidates[0]

                    # Ищем преподавателя
                    teacher_candidates = [line for line in lines if any(word in line.lower() for word in ['преподаватель', 'преп.'])]
                    if teacher_candidates:
                        event_data['parsed']['teacher'] = teacher_candidates[0]

        except Exception as e:
            logger.warning(f"Ошибка детального парсинга события: {e}")

        return event_data


async def update_schedule_daily():
    """Функция для ежедневного обновления расписания"""
    parser = UniversityParser(headless=True, use_saved_session=True)
    success = await parser.parse_and_save_schedule()
    return success
