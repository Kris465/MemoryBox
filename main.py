'''
My try to parse the big website
'''

from bs4 import BeautifulSoup
import requests

# URL = 'https://www.novelupdates.com/series/sss-grade-cafe-in-front-of-the-dungeon/?pg=8#myTable'
# html_text = requests.get(URL).text
# soup = BeautifulSoup(html_text, 'lxml')
# link = soup.find('div', class_='two-thirds')
# print(link)

URL = 'https://www.novelupdates.com/series/sss-grade-cafe-in-front-of-the-dungeon/?pg=8#myTable'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
page = requests.get(URL, headers=headers)
print(page.status_code)
needed_text = []
soup = BeautifulSoup(page.text, "lxml")
table = soup.find_all('a', class_ = 'chp-release')
print(table)
