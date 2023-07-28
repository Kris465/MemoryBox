# import random
# import time
from bs4 import BeautifulSoup
import requests

from writer_to_json import write


def get_chapters():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                                AppleWebKit/537.36 (KHTML, like Gecko)\
                                Chrome/111.0.0.0 Safari/537.36'}
    title = input("title: ")
    url = input("url: ")
    number = 55
    all_chapters = {}
    while url is not None:
    # while number <= 80:
        response = requests.get(url, headers=headers)
        print(response.status_code)
        soup = BeautifulSoup(response.text, 'lxml')
        # time.sleep(random.randint(5, 40))
        result = soup.find_all("div", class_="reading-content")
        temp_dict = {number: url + i.text for i in result}
        print(temp_dict)
        all_chapters.update(temp_dict)
        links = soup.find_all("a")
        for link in links:
            if "next" in link.text.lower() and link["href"] != "#":
                try:
                    next_link = link['href']
                except Exception:
                    next_link = input("url: ")
                break
            else:
                next_link = None
        number += 1
        url = next_link
        # url = "https://www.wuxiap.com" + next_link
        # url = "https://rainofsnow.com" + next_link
        # url = "https://puretl.com" + next_link
        # url = "https://travistranslations.com" + next_link
        # url = "https://www.wuxiaworld.eu" + next_link

    write(f"{title}", all_chapters)


get_chapters()
