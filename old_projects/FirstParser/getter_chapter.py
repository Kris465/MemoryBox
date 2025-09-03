'''
https://tproger.ru/translations/skraping-sajta-s-pomoshhju-python-gajd-dlja-novichkov/
'''

import requests
from bs4 import BeautifulSoup

def getter_chapter(URL):
    '''
    This function gets text from the webpage
    '''
    html_text = requests.get(URL).text
    soup = BeautifulSoup(html_text, 'lxml')
    ad = soup.find('div', class_ = "entry-content").text
    return ad
