from bs4 import BeautifulSoup
import requests

# Получаем HTML-код страницы
url = 'https://mesmerizingmemoirs.com/novel/she-was-sent-by-god/ss-01/'
html = requests.get(url).text

# Создаем объект BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Ищем все ссылки на странице
links = soup.find_all('a')

# Ищем ссылку со словом "next"
for link in links:
    if 'next' in link.text.lower():
        next_url = link['href']
        print('Ссылка на следующую страницу:', next_url)
        break
