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
        time.sleep(3)

        # Ждем конкретный элемент
        try:
            page.wait_for_selector('//*[@id="main"]/div/div/div[4]/div[2]/div/div/div', timeout=10000)
            print("Целевой элемент найден")
        except:
            print("Элемент не найден, но продолжаем")

        # Плавный скролл до самого низа
        print("Начинаем плавный скролл...")
        scroll_to_bottom(page)
        time.sleep(3)

        html_content = page.content()

        with open('page.html', 'w', encoding='utf-8') as file:
            file.write(html_content)

        print('Верстка успешно сохранена в файл page.html')
        print(f'Размер HTML: {len(html_content)} символов')

        # БРАУЗЕР НЕ ЗАКРЫВАЕТСЯ АВТОМАТИЧЕСКИ!
        print("Браузер остается открытым. Закройте его вручную когда закончите.")
        
        # Бесконечный цикл чтобы скрипт не завершался
        while True:
            time.sleep(1)

        return html_content


def scroll_to_bottom(page):
    # Плавный скролл до низа
    page.evaluate("""
        () => {
            window.scrollTo({
                top: document.documentElement.scrollHeight,
                behavior: 'smooth'
            });
        }
    """)
    # Даем время на скролл и подгрузку контента
    time.sleep(8)
    
    # Дополнительная проверка и скролл если нужно
    is_at_bottom = page.evaluate("""
        () => window.innerHeight + window.scrollY >= document.documentElement.scrollHeight - 100
    """)
    
    if not is_at_bottom:
        print("Еще не внизу, скроллим еще раз...")
        page.evaluate("""
            () => {
                window.scrollTo({
                    top: document.documentElement.scrollHeight,
                    behavior: 'smooth'
                });
            }
        """)
        time.sleep(5)


if __name__ == "__main__":
    load_dotenv(find_dotenv())
    url = os.getenv("URL")
    print(f"Загружаем URL: {url}")
    html = get_page_html(url)
