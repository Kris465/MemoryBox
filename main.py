import os
from playwright.sync_api import sync_playwright
import time
from dotenv import load_dotenv, find_dotenv
import json


def get_page_data(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.set_viewport_size({"width": 1200, 'height': 800})

        page.goto(url, timeout=60000)
        page.wait_for_load_state('domcontentloaded')
        page.wait_for_load_state('load')
        time.sleep(3)

        try:
            page.wait_for_selector(
                '//*[@id="main"]/div/div/div[4]/div[2]/div/div/div',
                timeout=10000)
            print("Целевой элемент найден")
        except:
            print("Элемент не найден, но продолжаем")

        print("Начинаем плавный скролл...")
        scroll_to_bottom(page)
        time.sleep(3)

        # Извлекаем данные через JavaScript
        print("Извлекаем данные...")
        extracted_data = page.evaluate("""
            () => {
                const results = [];

                // Ищем все элементы внутри целевого контейнера
                const container = document.querySelector('#main div div div:nth-child(4) div:nth-child(2) div div div');
                if (!container) {
                    console.log('Контейнер не найден');
                    return results;
                }

                // Ищем все дочерние элементы с данными
                const items = container.querySelectorAll('div > div');

                items.forEach((item, index) => {
                    // Извлекаем нужные данные из каждого элемента
                    results.push({
                        id: index,
                        text: item.innerText.trim(),
                        html: item.innerHTML,
                        class: item.className,
                        tag: item.tagName
                        // Добавьте другие нужные поля
                    });
                });

                return results;
            }
        """)
        
        print(extracted_data)

        # Сохраняем данные в JSON
        with open('extracted_data.json', 'w', encoding='utf-8') as file:
            json.dump(extracted_data, file, ensure_ascii=False, indent=2)

        # Также сохраняем HTML для сравнения
        html_content = page.content()
        with open('page.html', 'w', encoding='utf-8') as file:
            file.write(html_content)

        print('Данные успешно сохранены в extracted_data.json')
        print(f'Собрано {len(extracted_data)} элементов')
        print(f'Размер HTML: {len(html_content)} символов')

        input("Нажмите Enter чтобы закрыть браузер...")
        browser.close()

        return extracted_data


def scroll_to_bottom(page):
    page.evaluate("""
        () => {
            window.scrollTo({
                top: document.documentElement.scrollHeight,
                behavior: 'smooth'
            });
        }
    """)
    time.sleep(8)

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
    data = get_page_data(url)
