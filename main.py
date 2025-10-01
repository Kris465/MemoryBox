from playwright.sync_api import sync_playwright
from loguru import logger
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')
logger.info("Запуск браузера...")

with sync_playwright() as p:
    logger.add("file.log",
               format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
               rotation="3 days", backtrace=True, diagnose=True)

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://adminbook.top-academy.ru/#/")
    logger.info("Страница загружена")

    page.wait_for_selector('input[name="username"]', timeout=10000)

    page.fill('input[name="username"]', LOGIN)
    page.fill('input[name="password"]', PASSWORD)
    logger.info("Данные для входа введены")

    page.click('button[type="submit"]')
    logger.info("Кнопка входа нажата")

    page.wait_for_timeout(5000)

    logger.success(f"Вход выполнен! Текущий URL: {page.url}")

    page.click('div.toggle_aside')
    logger.info("Боковая панель открыта")
    page.wait_for_timeout(1000)

    input("Вход выполнен. Нажмите Enter для закрытия...")

    browser.close()
