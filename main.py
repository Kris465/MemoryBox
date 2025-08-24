import os
from playwright.sync_api import sync_playwright
import time
from dotenv import load_dotenv, find_dotenv


def get_page_html(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.set_viewport_size({"width": 1200, 'height': 800})

        page.goto(url, timeout=60000)
        page.wait_for_load_state('networkidle')
        time.sleep(2)

        print("Начало скролла")
        scroll_to_bottom(page)
        time.sleep(3)
        
        html_content = page.content()

        with open('page.html', 'w', encoding='utf-8') as file:
            file.write(html_content)

        print('Верстка успешно сохранена в файл page.html')
        print(f'Размер HTML: {len(html_content)} символов')
        
        browser.close()
        return html_content


def scroll_to_bottom(page):
    last_height = page.evaluate("() => document.documentElement.scrollHeight")
    print(f"Начальная высота: {last_height}px")

    scroll_attempts = 0
    max_attempts = 20

    while scroll_attempts < max_attempts:
        page.evaluate("window.scrollTo(0, document.documentElement.scrollHeight)")
        time.sleep(1.5)
        
        new_height = page.evaluate("() => document.documentElement.scrollHeight")
        print(f"Высота после скролла #{scroll_attempts + 1}: {new_height}px")

        if new_height == last_height:
            print("Достигнута максимальная высота")
            break

        last_height = new_height
        scroll_attempts += 1


if __name__ == "__main__":
    load_dotenv(find_dotenv())
    url = os.getenv("URL")
    print(f"Загружаем URL: {url}")
    html = get_page_html(url)
