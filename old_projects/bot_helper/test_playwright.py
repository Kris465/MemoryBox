import asyncio
from playwright.async_api import async_playwright
from loguru import logger


async def save_page_html(url, selector=None):
    """
    Сохраняет HTML страницы в файл для анализа
    """
    try:
        async with async_playwright() as playwright:
            browser = await playwright.chromium.launch(headless=True)  # headless=False чтобы видеть браузер
            context = await browser.new_context()
            page = await context.new_page()

            logger.info(f"Перехожу на: {url}")
            await page.goto(url, wait_until='domcontentloaded')

            await page.wait_for_timeout(5000)

            if selector:
                logger.info(f"Ищу селектор: {selector}")
                try:
                    await page.wait_for_selector(selector, timeout=10000)
                    logger.success(f"Селектор {selector} найден!")
                except Exception as e:
                    logger.error(f"Селектор {selector} не найден: {e}")

            html = await page.content()

            filename = url.split('//')[1].replace('/', '_').replace('.', '_') + '.html'
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(html)

            logger.success(f"HTML сохранен в файл: {filename}")

            cleaned_filename = f"cleaned_{filename}"
            with open(cleaned_filename, 'w', encoding='utf-8') as f:
                f.write(html[:5000] + "\n\n... [содержимое обрезано для удобства] ...")

            logger.info(f"Укороченная версия сохранена в: {cleaned_filename}")

            await context.close()
            await browser.close()

            return filename
    except Exception as e:
        logger.error(f"Ошибка при сохранении HTML: {e}")
        return None


async def analyze_page_structure(url):
    """
    Анализирует структуру страницы и ищет возможные селекторы
    """
    try:
        async with async_playwright() as playwright:
            browser = await playwright.chromium.launch(headless=True)
            context = await browser.new_context()
            page = await context.new_page()

            await page.goto(url)
            await page.wait_for_timeout(3000)

            # Ищем все ссылки на странице
            links = await page.evaluate('''() => {
                const allLinks = Array.from(document.querySelectorAll('a'));
                return allLinks.map(link => ({
                    text: link.textContent.trim(),
                    href: link.href,
                    class: link.className,
                    id: link.id,
                    outerHTML: link.outerHTML
                })).filter(link => link.text && link.href);
            }''')
            
            logger.info(f"Найдено ссылок: {len(links)}")
            
            # Фильтруем ссылки, которые могут быть "next chapter"
            next_links = []
            next_keywords = ['next', 'следующая', 'глава', 'chapter', '→', '>', 'continue', 'read']
            
            for link in links:
                lower_text = link['text'].lower()
                if any(keyword in lower_text for keyword in next_keywords):
                    next_links.append(link)
            
            logger.info(f"Потенциальные ссылки 'next': {len(next_links)}")
            
            # Сохраняем информацию о ссылках
            with open('link_analysis.txt', 'w', encoding='utf-8') as f:
                f.write(f"Анализ ссылок для: {url}\n")
                f.write("=" * 50 + "\n\n")
                
                f.write("ВСЕ ССЫЛКИ:\n")
                for i, link in enumerate(links[:20], 1):  # первые 20 ссылок
                    f.write(f"{i}. {link['text']} -> {link['href']}\n")
                    f.write(f"   Class: {link['class']}\n")
                    f.write(f"   ID: {link['id']}\n")
                    f.write(f"   HTML: {link['outerHTML'][:100]}...\n")
                    f.write("-" * 30 + "\n")
                
                f.write("\n\nПОТЕНЦИАЛЬНЫЕ 'NEXT' ССЫЛКИ:\n")
                for i, link in enumerate(next_links, 1):
                    f.write(f"{i}. {link['text']} -> {link['href']}\n")
                    f.write(f"   Class: {link['class']}\n")
                    f.write(f"   ID: {link['id']}\n")
                    f.write(f"   HTML: {link['outerHTML']}\n")
                    f.write("-" * 50 + "\n")
            
            logger.success("Анализ ссылок сохранен в link_analysis.txt")
            
            await context.close()
            await browser.close()
            
    except Exception as e:
        logger.error(f"Ошибка при анализе структуры: {e}")


async def main():
    # Настройка логгера
    logger.add("debug.log", format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}", level="DEBUG")

    url = "https://hyacinthbloom.com/the-main-character-is-obsessed-with-a-foreign-substance/the-main-character-is-obsessed-with-a-foreign-substance-chapter-1-1/"
    selector = ".bottomnav a"
    logger.info("Запуск тестового анализа...")

    # Вариант 1: Просто сохранить HTML
    print("1. Сохранение HTML страницы...")
    html_file = await save_page_html(url, selector)

    # Вариант 2: Детальный анализ структуры
    print("\n2. Анализ структуры страницы...")
    await analyze_page_structure(url)

    print("\n3. Готово! Проверьте файлы:")
    if html_file:
        print(f"   - {html_file} (полный HTML)")
        print(f"   - cleaned_{html_file} (укороченная версия)")
    print("   - link_analysis.txt (анализ ссылок)")

if __name__ == "__main__":
    asyncio.run(main())
