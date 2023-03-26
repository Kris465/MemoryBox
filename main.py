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
page = requests.get(URL)
print(page.status_code)
needed_text = []

soup = BeautifulSoup(page.text, "lxml")
print(soup.find_all("p"))
