import feedparser
import requests
from loguru import logger


def get_news(limit: int = 5):
    url = "https://www.theguardian.com/world/rss" 
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except Exception as e:
        logger.error(f"Ошибка при загрузке RSS: {e}")
        return []

    feed = feedparser.parse(response.content)

    if not feed.entries:
        logger.warning("Новостей не найдено — возможно, проблема с RSS")
        return []

    return [
        {"title": entry.title, "url": entry.link}
        for entry in feed.entries[:limit]
    ]
