'''
This module parses wordpess pages going by strings in json file
'''
import requests
from bs4 import BeautifulSoup

def getter_chapter(URL):
    '''
    This function gets text from the webpage
    '''
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
    page = requests.get(URL, headers=headers).text # pylint: disable=W3101
    soup = BeautifulSoup(page, 'lxml')
    ad = soup.find('div', class_ = "entry-content").text
    return ad
