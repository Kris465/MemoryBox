'''
https://tproger.ru/translations/skraping-sajta-s-pomoshhju-python-gajd-dlja-novichkov/
'''

import requests
from bs4 import BeautifulSoup
from re import sub
from decimal import Decimal
import io
from datetime import datetime
import pandas as pd

URL = 'https://cabinfourtranslations.wordpress.com/2022/07/15/sss-grade-cafe-in-front-of-the-dungeon-chapter-1/'
html_text = requests.get(URL).text
soup = BeautifulSoup(html_text, 'lxml')
ad = soup.find('div', class_ = "entry-content").text
print(ad)
