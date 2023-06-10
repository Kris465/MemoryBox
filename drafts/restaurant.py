from bs4 import BeautifulSoup
import requests


def parse():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                        AppleWebKit/537.36 (KHTML, like Gecko)\
                        Chrome/111.0.0.0 Safari/537.36'}
    url = "https://www.tripadvisor.com/Restaurant_Review-g187147-d21389323-Reviews-Restaurant_Pizzamore-Paris_Ile_de_France.html"
    page = requests.get(url, headers=headers)
    print(page.status_code)
    soup = BeautifulSoup(page.text, "lxml")
    containers = soup.find_all("div", "review-container")
    for container in containers:
        print(container.text)
    return containers


parse()
