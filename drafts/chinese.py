import requests
from bs4 import BeautifulSoup

from drafts.writer_to_json import write

title = 'Second Marriage in the 1970s'
url = 'https://www.shubaow.net/85_85206/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                           AppleWebKit/537.36 (KHTML, like Gecko)\
                           Chrome/111.0.0.0 Safari/537.36'}
number = 1
all_chapters = {}

response = requests.get(url, headers=headers)
print(response.status_code)
soup = BeautifulSoup(response.text, 'html.parser')
chapter_links = soup.find_all('a')

for link in chapter_links:
    if 'href' in link.attrs:
        chapter_url = 'https:/' + link['href']
        print(chapter_url)
        try:
            chapter_response = requests.get(chapter_url, headers=headers)
            if chapter_response.status_code == 200:
                chapter_response.encoding = chapter_response.apparent_encoding
                chapter_soup = BeautifulSoup(chapter_response.text,
                                             'html.parser')
                chapter = chapter_soup.find_all('div', 'content_read')
                temp_dict = {number: ch.text for ch in chapter}
                all_chapters.update(temp_dict)
                write(title, all_chapters)
            else:
                print(f"Chapter {number} not found")
        except Exception:
            print(f"Error while processing chapter {number}")
        number += 1
