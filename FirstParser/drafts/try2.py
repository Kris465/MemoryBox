import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

URL_TEMPLATE = "https://cabinfourtranslations.wordpress.com/2022/07/15/sss-grade-cafe-in-front-of-the-dungeon-chapter-1/"
r = requests.get(URL_TEMPLATE)
print(r.status_code)
print(r.text)

soup = bs(r.text, "html.parser")
looking_for = soup.find_all('h2', class_ = 'screen-reader-text')
for i in looking_for:
    print(i.a['title'])
