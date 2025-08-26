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

        page.goto(url, timeout=120000)  # Увеличиваем таймаут для Notion
        time.sleep(5)  # Даем время на первоначальную загрузку

        # Ждем загрузки контента Notion
        page.wait_for_load_state('networkidle')
        time.sleep(3)

        print("Начинаем скролл для подгрузки всего контента...")
        scroll_to_bottom(page)
        time.sleep(5)

        # Извлекаем структурированные данные из Notion
        print("Извлекаем данные из Notion таблицы...")
        notion_data = page.evaluate("""
            () => {
                const results = [];
                
                // Ищем все таблицы Notion
                const tables = document.querySelectorAll('[data-content-entity-type="collection"]');
                console.log('Найдено таблиц Notion:', tables.length);
                
                tables.forEach((table, tableIndex) => {
                    const tableData = {
                        table_number: tableIndex + 1,
                        rows: []
                    };
                    
                    // Ищем строки в таблице
                    const rows = table.querySelectorAll('.notion-table-view-row');
                    console.log('В таблице', tableIndex + 1, 'найдено строк:', rows.length);
                    
                    rows.forEach((row, rowIndex) => {
                        const rowData = {
                            row_number: rowIndex + 1,
                            cells: []
                        };
                        
                        // Ищем ячейки в строке
                        const cells = row.querySelectorAll('.notion-table-cell');
                        
                        cells.forEach((cell, cellIndex) => {
                            const cellData = {
                                cell_number: cellIndex + 1,
                                text: cell.innerText.trim(),
                                type: 'text'
                            };
                            
                            // Проверяем тип содержимого
                            if (cell.querySelector('img')) {
                                cellData.type = 'image';
                                cellData.image_url = cell.querySelector('img').src;
                            } else if (cell.querySelector('a')) {
                                cellData.type = 'link';
                                const link = cell.querySelector('a');
                                cellData.link_url = link.href;
                                cellData.link_text = link.innerText.trim();
                            } else if (cell.querySelector('input[type="checkbox"]')) {
                                cellData.type = 'checkbox';
                                cellData.checked = cell.querySelector('input[type="checkbox"]').checked;
                            }
                            
                            rowData.cells.push(cellData);
                        });
                        
                        tableData.rows.push(rowData);
                    });
                    
                    results.push(tableData);
                });
                
                return results;
            }
        """)

        # Если не нашли таблиц, пробуем альтернативный подход
        if not notion_data or not any(len(table['rows']) > 0 for table in notion_data):
            print("Пробуем альтернативный метод сбора данных...")
            notion_data = page.evaluate("""
                () => {
                    const results = [];

                    // Ищем все элементы с данными
                    const dataElements = document.querySelectorAll('.notion-page-content > div > div');

                    dataElements.forEach((element, index) => {
                        results.push({
                            element_number: index + 1,
                            text: element.innerText.trim(),
                            html: element.outerHTML,
                            class: element.className
                        });
                    });

                    return results;
                }
            """)

        print(f"Извлечено данных: {len(notion_data)} элементов")

        # Сохраняем данные в JSON
        with open('notion_data.json', 'w', encoding='utf-8') as file:
            json.dump(notion_data, file, ensure_ascii=False, indent=2)

        print('Данные успешно сохранены в notion_data.json')

        # Также сохраняем HTML для отладки
        html_content = page.content()
        with open('notion_page.html', 'w', encoding='utf-8') as file:
            file.write(html_content)

        input("Нажмите Enter чтобы закрыть браузер...")
        browser.close()

        return notion_data


def scroll_to_bottom(page):
    print("Начинаем скролл...")
    scroll_attempts = 0
    max_attempts = 15

    while scroll_attempts < max_attempts:
        prev_height = page.evaluate("() => document.documentElement.scrollHeight")
        page.evaluate("""
            () => {
                window.scrollTo({
                    top: document.documentElement.scrollHeight,
                    behavior: 'smooth'
                });
            }
        """)

        # Ждем подгрузки контента
        time.sleep(3)

        # Проверяем новую высоту
        new_height = page.evaluate("() => document.documentElement.scrollHeight")

        print(f"Скролл {scroll_attempts + 1}: было {prev_height}, стало {new_height}")

        if new_height == prev_height:
            print("Высота не изменилась - завершаем скролл")
            break

        scroll_attempts += 1

    # Дополнительный скролл для уверенности
    page.evaluate("window.scrollTo(0, 0)")
    time.sleep(1)
    page.evaluate("window.scrollTo(0, document.documentElement.scrollHeight)")
    time.sleep(2)


if __name__ == "__main__":
    load_dotenv(find_dotenv())
    url = os.getenv("URL")
    data = get_page_data(url)
