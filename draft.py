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

        print("Начинаем плавный скролл...")
        scroll_to_bottom(page)
        time.sleep(3)

        # Извлекаем данные из таблицы
        print("Извлекаем данные из таблицы...")
        table_data = page.evaluate("""
            () => {
                const results = [];
                
                // Находим таблицу по вашему селектору
                const table = document.querySelector('#main > div > div > div:nth-child(4) > div:nth-child(2) > div > div > div > div:nth-child(3)');
                if (!table) {
                    console.log('Таблица не найдена');
                    return results;
                }
                
                // Ищем все строки таблицы
                const rows = table.querySelectorAll('div.notion-table-view-row');
                console.log('Найдено строк:', rows.length);
                
                rows.forEach((row, rowIndex) => {
                    const rowData = {
                        row_number: rowIndex + 1,
                        cells: []
                    };
                    
                    // Ищем все ячейки в строке
                    const cells = row.querySelectorAll('div > div');
                    
                    cells.forEach((cell, cellIndex) => {
                        const cellData = {
                            cell_number: cellIndex + 1,
                            text: cell.innerText.trim(),
                            html: cell.innerHTML,
                            class: cell.className,
                            links: []
                        };
                        
                        // Извлекаем ссылки из ячейки
                        const links = cell.querySelectorAll('a');
                        links.forEach(link => {
                            cellData.links.push({
                                text: link.innerText.trim(),
                                href: link.href,
                                title: link.title
                            });
                        });
                        
                        rowData.cells.push(cellData);
                    });
                    
                    results.push(rowData);
                });
                
                return results;
            }
        """)

        print(f"Извлечено {len(table_data)} строк таблицы")

        # Сохраняем данные в JSON
        with open('table_data.json', 'w', encoding='utf-8') as file:
            json.dump(table_data, file, ensure_ascii=False, indent=2)

        print('Данные таблицы успешно сохранены в table_data.json')

        input("Нажмите Enter чтобы закрыть браузер...")
        browser.close()

        return table_data


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
