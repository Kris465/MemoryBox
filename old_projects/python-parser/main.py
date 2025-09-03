import json
import cloudscraper
from bs4 import BeautifulSoup


def get_chapter_page(url):
    scraper = cloudscraper.create_scraper()

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    }

    cookies = {
        "PHPSESSID": "0e1fc6361290818444e114e964131979",
        "cf_clearance": "wVqW5U8X4ARKWJUh3S9rpwChtmwcntycvBlixTfVipQ-1722170638-1.0.1.1-M38Z06EmIx_4XYMGbO9FSc1m__uaAWLJXAnVeYcTb5S7WbhDSRI6KvolP5sb_butVuFK.W.AmW.iuyCk5n5vEg",
        "quads_browser_width": "1920",
        "quads_browser_width": "1920",
        "wpmanga-reading-history": "W3siaWQiOjIwOTYsImMiOiIzNjQ1IiwicCI6MSwiaSI6IiIsInQiOjE3MjIxNzA2NDF9XQ%3D%3D"
    }

    response = scraper.get(url, headers=headers, cookies=cookies)

    if response.status_code == 200:
        return response.text
    else:
        print(f"Ошибка: {response.status_code}")
        return None


def text_getter(chapter_text, chapter_number):
    soup = BeautifulSoup(chapter_text, 'html.parser')
    text = soup.find('div', class_='reading-content')
    temp_dict = {chapter_number: url + text.text}
    return temp_dict


def get_next_link(chapter_text):
    soup = BeautifulSoup(chapter_text, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        if 'next' in link.text.lower():
            next_link = link['href']
            next_link.strip()
            return next_link
        else:
            return None


url = "https://guavaread.com/novel/i-became-my-sons-first-love/chapter-46/"
chapter_number = 46
chapters = {}
while url is not None:
    chapter_page = get_chapter_page(url)
    chapter = text_getter(chapter_page, chapter_number)
    chapters.update(chapter)
    url = get_next_link(chapter_page)
    with open('chapters.json', 'w', encoding='utf-8') as file:
        json.dump(chapters, file, ensure_ascii=False, indent=4)
