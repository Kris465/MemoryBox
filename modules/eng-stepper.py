from bs4 import BeautifulSoup
import requests

from writer_to_json import write


def get_chapters():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                                AppleWebKit/537.36 (KHTML, like Gecko)\
                                Chrome/111.0.0.0 Safari/537.36'}
    title = input("title: ")
    url = input("url: ")
    number = 54
    all_chapters = {}
    # while url is not None:
    while number < 61:
        response = requests.get(url, headers=headers)
        print(response.status_code)
        soup = BeautifulSoup(response.text, 'lxml')
        result = soup.find_all("div", class_="zoomdesc-cont")
        temp_dict = {number: i.text for i in result}
        print(temp_dict)
        all_chapters.update(temp_dict)
        soup = BeautifulSoup(response.text, "lxml")
        links = soup.find_all("a")
        for link in links:
            if "next" in link.text.lower():
                next_link = link['href']
                print(next_link)
                break
            else:
                next_link = None
        number += 1
        if next_link is None:
            url = input("url: ")
        else:
            url = next_link
            # url = "https://puretl.com" + next_link

    write(f"{title}", all_chapters)


get_chapters()
