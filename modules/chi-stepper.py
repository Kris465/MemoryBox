from bs4 import BeautifulSoup
import requests

from writer_to_json import write
from writer_to_txt import write_txt


def get_chapters():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                                AppleWebKit/537.36 (KHTML, like Gecko)\
                                Chrome/111.0.0.0 Safari/537.36'}
    title = input("title: ")
    url = input("url: ")
    all_pages = {}
    number = 1
    while url is not None:
        response = requests.get(url, headers=headers)
        response.encoding = response.apparent_encoding
        print(response.status_code)
        soup = BeautifulSoup(response.text, 'html.parser')
        result = soup.find("div", id="BookContent")
        print(result.text)
        temp_dict = {str(number): url + result.text}
        all_pages.update(temp_dict)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all("a")
        for link in links:
            if "下壹頁" in link.text:
                next_link = link['href']
                print(next_link)
                break
            else:
                next_link = None
        number += 1
        if next_link is None:
            url = input("url: ")
            if url == '':
                break
        else:
            url = "https://www.sto.cx" + next_link

    write(f"{title}", all_pages, language="chi")


get_chapters()
