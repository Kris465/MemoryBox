import requests
from bs4 import BeautifulSoup


def get_ria_news(keyword: str, limit=5):
    url = f"https://ria.ru/search/?query={keyword}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    news_items = soup.find_all("a", class_="list-item__title", limit=limit)
    news = []

    for item in news_items:
        title = item.text.strip()
        link = item['href']
        news.append({"title": title, "url": link})

    return news
