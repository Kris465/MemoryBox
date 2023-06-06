import random
import time
import requests
from bs4 import BeautifulSoup
import re
from modules.reader_from_json import read
from modules.writer_to_json import write


def parse_links():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                                AppleWebKit/537.36 (KHTML, like Gecko)\
                                Chrome/111.0.0.0 Safari/537.36'}
    url = input("url: ")
    path = re.sub(r'^https?://[^/]+', '', url)
    time.sleep(random.randint(10, 120))
    response = requests.get(url, headers=headers)
    print(response.status_code)
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, 'html.parser')

    links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and href.startswith(path):
            links.append(href)

    sorted_links = sorted(set(links))

    write("links", {"ch" + str(i):
                    link for i, link in enumerate(sorted_links)})


def collect_chapters():
    title = input("Title: ")
    links_dict = read("links")
    all_chapters = {}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                                AppleWebKit/537.36 (KHTML, like Gecko)\
                                Chrome/111.0.0.0 Safari/537.36'}

    for k, v in links_dict.items():
        time.sleep(random.randint(20, 120))
        response = requests.get('https://www.shubaow.net' + v, headers=headers)
        print(response.status_code)
        response.encoding = response.apparent_encoding
        soup = BeautifulSoup(response.text, 'html.parser')
        chapter_text = soup.find('div', "content_read").text
        temp_dict = {k: chapter_text}
        print(k)
        all_chapters.update(temp_dict)
        write(title, all_chapters)


parse_links()
collect_chapters()
