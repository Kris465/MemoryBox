from playwright.sync_api import sync_playwright
import time
import json
import re


def get_page_data(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.set_viewport_size({"width": 1200, 'height': 800})

        page.goto(url, timeout=120000)
        time.sleep(8)

        print("Начинаем скролл и загрузку данных...")
        all_data = scroll_and_collect_data(page)
        time.sleep(3)

        print(f"Успешно извлечено строк: {len(all_data)}")

        with open('yonote_data.json', 'w', encoding='utf-8') as file:
            json.dump(all_data, file, ensure_ascii=False, indent=2)

        print('Данные успешно сохранены в yonote_data.json')

        input("Нажмите Enter чтобы закрыть браузер...")
        browser.close()

        return all_data


def has_load_more_button(page):
    """Проверяет наличие кнопки загрузки с любым двузначным числом"""
    try:
        buttons = page.query_selector_all('button')
        for button in buttons:
            button_text = button.inner_text()
            if re.match(r'^Загрузить \d{1,2} строк', button_text):
                return button
        return None
    except:
        return None


def scroll_and_collect_data(page):
    """Постепенно скроллим и собираем данные"""
    print("Скролл и сбор данных...")

    max_attempts = 250
    loaded_count = 0
    all_data = []
    processed_rows = set()

    for i in range(max_attempts):
        try:
            current_data = extract_visible_data(page, processed_rows)
            all_data.extend(current_data)

            load_more_button = has_load_more_button(page)

            if load_more_button and load_more_button.is_visible():
                load_more_button.click()
                loaded_count += 1
                time.sleep(3.5)
                print(f"\rИтерация {i+1}/{max_attempts}, загрузок: {loaded_count}, собрано строк: {len(all_data)}", end="", flush=True)
            else:
                # Скроллим вниз
                page.evaluate("window.scrollBy(0, 400)")
                time.sleep(1.5)
                print(f"\rИтерация {i+1}/{max_attempts}, загрузок: {loaded_count}, собрано строк: {len(all_data)}", end="", flush=True)   
        except Exception as e:
            page.evaluate("window.scrollBy(0, 400)")
            time.sleep(1.5)

        is_bottom = page.evaluate("""
            () => {
                const scrollHeight = document.documentElement.scrollHeight;
                const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
                const clientHeight = document.documentElement.clientHeight;
                return scrollTop + clientHeight >= scrollHeight - 100;
            }
        """)

        if is_bottom:
            final_check = has_load_more_button(page)
            if not final_check:
                print("\nДостигнут конец страницы")
                break

            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(3)
            final_data = extract_visible_data(page, processed_rows)
            all_data.extend(final_data)

            final_check_again = has_load_more_button(page)
            if not final_check_again:
                print("\nПосле полного скролла кнопка не найдена - завершаем")
                break

    time.sleep(2)
    final_data = extract_visible_data(page, processed_rows)
    all_data.extend(final_data)
    print("\nВыполняем финальную проверку...")
    page.evaluate("window.scrollTo(0, 0)")
    time.sleep(2)

    scroll_height = page.evaluate("document.documentElement.scrollHeight")
    current_position = 0
    scroll_step = 300

    while current_position < scroll_height:
        page.evaluate(f"window.scrollTo(0, {current_position})")
        time.sleep(0.8)
        current_position += scroll_step

        extra_data = extract_visible_data(page, processed_rows)
        if extra_data:
            all_data.extend(extra_data)
            print(f"\rФинальная проверка: собрано {len(all_data)} строк", end="", flush=True)

    unique_data = []
    seen_indices = set()
    for item in all_data:
        if item['row_index'] not in seen_indices:
            unique_data.append(item)
            seen_indices.add(item['row_index'])

    print(f"\nЗавершено. Всего загрузок: {loaded_count}, уникальных строк: {len(unique_data)}")
    return unique_data


def extract_visible_data(page, processed_rows):
    """Извлекаем данные только из видимых строк, которые еще не обработаны"""
    data = page.evaluate("""
        () => {
            const results = [];
            const rows = document.querySelectorAll('[data-testid^="tableRow"]');

            for (let rowIndex = 1; rowIndex < rows.length; rowIndex++) {
                const row = rows[rowIndex];
                const row_index = row.getAttribute('data-row-index');

                const rowData = {
                    row_number: rowIndex,
                    row_index: row_index,
                    columns: {}
                };

                // Более специфичный селектор для основных ячеек
                const mainCells = row.querySelectorAll('div[class*="cellStyled"][style*="width: 160px"]');

                for (let i = 0; i < mainCells.length; i++) {
                    const cell = mainCells[i];

                    // Удаляем все кнопки и служебные элементы перед извлечением текста
                    const clone = cell.cloneNode(true);
                    const elementsToRemove = clone.querySelectorAll('button, .property-copy-button, .title-property-buttons');
                    elementsToRemove.forEach(el => el.remove());

                    let cellText = clone.innerText.trim();

                    if (cellText) {
                        const columnNames = [
                            'id', 'name', 'message', 'property_1', 'city_region',
                            'contact', 'occupation', 'comment', 'portfolio_instagram'
                        ];

                        if (i < columnNames.length) {
                            rowData.columns[columnNames[i]] = cellText;
                        } else {
                            rowData.columns[`column_${i + 1}`] = cellText;
                        }
                    }
                }
                results.push(rowData);
            }

            return results;
        }
    """)

    new_data = [item for item in data if item['row_index'] not in processed_rows]

    for item in new_data:
        processed_rows.add(item['row_index'])

    return new_data


if __name__ == "__main__":
    url = "https://mir-kreatorov.yonote.ru/share/f165d575-f0c5-4ca0-8e27-7712aa0b5af7/doc/baza-kreatorov-OlRJaWEG35?v=13e91c0b-5e84-4df6-870e-06f5fdd77073"
    print(f"Загружаем URL: {url}")
    data = get_page_data(url)
