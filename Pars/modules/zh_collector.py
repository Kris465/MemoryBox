import random
import time
import requests
from bs4 import BeautifulSoup
from reader_from_json import read
from writer_to_json import write


def parse_links():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                                AppleWebKit/537.36 (KHTML, like Gecko)\
                                Chrome/111.0.0.0 Safari/537.36'}
    url = input("url: ")
    response = requests.get(url, headers=headers)
    print(response.status_code)
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, 'html.parser')

    links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        print(href)
        links.append(href)

    sorted_links = sorted(set(links))

    write("links", {str(i):
                    link for i, link in enumerate(sorted_links)})


def collect_chapters():
    title = input("Title: ")
    links_dict = read("links")
    all_chapters = {}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                                AppleWebKit/537.36 (KHTML, like Gecko)\
                                Chrome/111.0.0.0 Safari/537.36'}

    for k, v in links_dict.items():
        time.sleep(random.randint(5, 60))
        response = requests.get('https://www.ddxs.com' + v, headers=headers)
        print(response.status_code)
        response.encoding = response.apparent_encoding
        soup = BeautifulSoup(response.text, 'html.parser')
        try:
            chapter_text = soup.find("dd", id="contents").text
        except Exception:
            chapter_text = " "
        # chapter_text = soup.find('div', "novelcontent").text
        temp_dict = {str(int(k) + 1): chapter_text}
        print(k)
        all_chapters.update(temp_dict)
        write(title, all_chapters, language="chi")


parse_links()
# collect_chapters()
