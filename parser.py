import os
from datetime import datetime
from dotenv import load_dotenv, find_dotenv
from playwright.async_api import async_playwright
from typing import Optional, Dict, Any
from loguru import logger


class UniversityParser:
    def __init__(self, headless: bool = True, use_saved_session: bool = True):
        load_dotenv(find_dotenv())
        self.login = os.getenv('LOGIN')
        self.password = os.getenv('PASSWORD')
        self.headless = headless
        self.use_saved_session = use_saved_session

        if not self.login or not self.password:
            raise ValueError("Логин или пароль не найдены в .env файле")

        self.browser = None
        self.context = None
        self.page = None
        self.playwright = None
        self.is_authenticated = False
        self.base_url = 'https://es.unitech-mo.ru/WebApp'

        logger.remove()
        logger.add(
            "university_bot.log",
            format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
            level="INFO",
            rotation="10 MB",
            retention="30 days"
        )

    async def __aenter__(self):
        await self.setup_browser()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()

    async def setup_browser(self):
        logger.info("Запускаем браузер...")

        self.playwright = await async_playwright().start()

        launch_options = {
            'headless': self.headless,
            'args': ['--no-sandbox', '--disable-dev-shm-usage']
        }

        self.browser = await self.playwright.chromium.launch(**launch_options)

        storage_state = None
        if self.use_saved_session and os.path.exists("auth_state.json"):
            logger.info("Используем сохраненную сессию")
            storage_state = "auth_state.json"

        context_options = {
            'viewport': {'width': 1920, 'height': 1080},
            'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        }

        if storage_state:
            context_options['storage_state'] = storage_state

        self.context = await self.browser.new_context(**context_options)
        self.page = await self.context.new_page()

    async def close(self):
        if self.browser:
            await self.browser.close()
        if self.playwright:
            await self.playwright.stop()

    async def get_schedule_for_date(self, target_date: datetime = None) -> Dict[str, Any]:
        """
        Получаем расписание на конкретную дату

        Args:
            target_date: Дата для получения расписания (по умолчанию сегодня)
        """
        if not target_date:
            target_date = datetime.now()

        logger.info(f"Получаем расписание на {target_date.strftime('%d.%m.%Y')}")

        try:
            if not await self._ensure_authenticated():
                return {'success': False, 'error': 'Ошибка авторизации'}

            if not await self._navigate_to_schedule():
                return {'success': False,
                        'error': 'Не удалось перейти к расписанию'}

            await self._select_date(target_date)
            schedule_data = await self._parse_schedule()

            return {
                'success': True,
                'date': target_date.strftime('%Y-%m-%d'),
                'schedule': schedule_data,
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }

        except Exception as e:
            logger.error(f"Ошибка при получении расписания: {e}")
            return {'success': False, 'error': str(e)}

    async def _ensure_authenticated(self) -> bool:
        """Обеспечиваем авторизацию"""
        if await self.check_current_auth_status():
            return True

        logger.info("Проходим авторизацию...")
        await self.page.goto(f'{self.base_url}/#/login', wait_until='networkidle')
        await self.page.wait_for_timeout(3000)

        inputs = await self.page.query_selector_all('input')
        if len(inputs) >= 2:
            await inputs[0].fill(self.login)
            await inputs[1].fill(self.password)
            await inputs[1].press('Enter')
            await self.page.wait_for_timeout(5000)

            if await self.check_current_auth_status():
                await self.context.storage_state(path="auth_state.json")
                return True

        return False

    async def check_current_auth_status(self) -> bool:
        """Проверяем статус авторизации"""
        try:
            await self.page.goto(f'{self.base_url}/#/', wait_until='networkidle', timeout=10000)
            await self.page.wait_for_timeout(2000)

            current_url = self.page.url
            if 'login' not in current_url.lower():
                self.is_authenticated = True
                return True

            return False
        except:
            return False

    async def _navigate_to_schedule(self) -> bool:
        """Переход к расписанию"""
        try:
            # Пробуем прямой URL
            await self.page.goto(f'{self.base_url}/#/Rasp/My', wait_until='networkidle')
            await self.page.wait_for_timeout(3000)

            # Проверяем, что мы на странице расписания
            page_content = await self.page.content()
            if any(word in page_content.lower() for word in ['расписание', 'schedule']):
                return True

            return False
        except Exception as e:
            logger.error(f"Ошибка перехода к расписанию: {e}")
            return False

    async def _select_date(self, target_date: datetime):
        """Выбираем дату в календаре"""
        try:
            # Ищем поле выбора даты
            date_selectors = [
                "input[type='date']",
                ".v-text-field__slot input",
                "[placeholder*='дату']",
                ".v-date-picker-table"
            ]
            
            for selector in date_selectors:
                if await self.page.is_visible(selector):
                    date_input = self.page.locator(selector).first
                    date_str = target_date.strftime('%Y-%m-%d')
                    await date_input.fill(date_str)
                    await self.page.wait_for_timeout(2000)
                    logger.info(f"Установлена дата: {date_str}")
                    break

        except Exception as e:
            logger.warning(f"Не удалось установить дату: {e}")

    async def _parse_schedule(self) -> Dict[str, Any]:
        """Парсим расписание с страницы"""
        try:
            await self.page.wait_for_timeout(3000)

            schedule_data = {
                'has_classes': False,
                'classes': [],
                'next_class_date': None,
                'group_info': None
            }

            group_elements = await self.page.query_selector_all('.v-card')
            for element in group_elements:
                text = await element.text_content()
                if text and 'БМЗ' in text:
                    schedule_data['group_info'] = text.strip()
                    break

            page_text = (await self.page.content()).lower()
            if 'расписание отсутствует' in page_text:
                if 'дата следующего занятия' in page_text:
                    import re
                    date_match = re.search(r'(\d{2}\.\d{2})', page_text)
                    if date_match:
                        schedule_data['next_class_date'] = date_match.group(1)

                return schedule_data

            class_selectors = [
                '.schedule-item',
                '.pair-item',
                '.rasp-item',
                '.v-card:has(.v-card__text)',
                '[class*="lesson"]',
                '[class*="pair"]'
            ]

            for selector in class_selectors:
                elements = await self.page.query_selector_all(selector)
                for element in elements:
                    class_info = await self._parse_class_element(element)
                    if class_info:
                        schedule_data['classes'].append(class_info)
                        schedule_data['has_classes'] = True

            return schedule_data

        except Exception as e:
            logger.error(f"Ошибка парсинга расписания: {e}")
            return {'has_classes': False, 'classes': [], 'error': str(e)}

    async def _parse_class_element(self, element) -> Optional[Dict[str, str]]:
        """Парсим информацию об одном занятии"""
        try:
            text = await element.text_content()
            if not text or len(text.strip()) < 10:
                return None

            lines = [line.strip() for line in text.split('\n') if line.strip()]

            class_info = {}

            for line in lines:
                if any(word in line.lower() for word in ['пара',
                                                         'урок']):
                    class_info['time'] = line
                elif any(word in line.lower() for word in ['ауд.',
                                                           'аудитория']):
                    class_info['room'] = line
                elif any(word in line.lower() for word in ['преподаватель',
                                                           'преп.']):
                    class_info['teacher'] = line
                elif len(line) > 5 and not any(word in line.lower() for word in ['расписание', 'группа']):
                    if 'subject' not in class_info:
                        class_info['subject'] = line

            return class_info if class_info else None

        except Exception as e:
            logger.warning(f"Ошибка парсинга элемента занятия: {e}")
            return None
