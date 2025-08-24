from playwright.sync_api import sync_playwright
import time


def get_page_html(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False
        )

        page = browser.new_page()

        try:
            page.goto(url, timeout=60000)

            page.wait_for_load_state('domcontentloaded')
            page.wait_for_load_state('load')
            time.sleep(2)

            html_content = page.content()

            with open('page.html', 'w', encoding='utf-8') as file:
                file.write(html_content)

            print('Верстка успешно сохранена в файл page.html')
            print(f'Размер HTML: {len(html_content)} символов')

            return html_content

        except Exception as e:
            print(f'Ошибка при загрузке страницы: {e}')
            return None

        finally:
            browser.close()


if __name__ == "__main__":
    url = "https://peaceful-mistake-74d.notion.site/dc60267701934e358e321ae08a222ff7?v=45a00aa67a8141289a8983fc89880aa6"
    html = get_page_html(url)
