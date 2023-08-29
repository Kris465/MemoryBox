from bs4 import BeautifulSoup
import requests

from writer_to_json import write


def get_chapters():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                                AppleWebKit/537.36 (KHTML, like Gecko)\
                                Chrome/111.0.0.0 Safari/537.36'}
    title = input("title: ")
    url = input("url: ")
    number = 81
    all_chapters = {}
    while url != '':
        response = requests.get(url, headers=headers)
        print(response.status_code)
        soup = BeautifulSoup(response.text, 'lxml')
        result = soup.find_all("div", class_="chapter-content")
        temp_dict = {number: url + i.text for i in result}
        print(temp_dict)
        all_chapters.update(temp_dict)
        url = input("url:")
        number += 1

    write(f"{title}", all_chapters)


get_chapters()
