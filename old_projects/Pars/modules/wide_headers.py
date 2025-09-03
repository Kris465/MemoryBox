import requests
from bs4 import BeautifulSoup

url = 'https://www.mtlnovel.com/the-master-of-metaphysics-is-the-movie-queen/chapter-25-1/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'Referer': 'https://www.google.com/'
}

response = requests.get(url, headers=headers)
print(response.status_code)
soup = BeautifulSoup(response.content, 'html.parser')
print(soup.text)
