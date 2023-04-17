'''
Parser module
input: string with link
output: <class 'bs4.element.ResultSet'>
'''

from bs4 import BeautifulSoup
import requests

def parser_(URL, tag, cl):
    '''
    It parses just one page
    '''
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
    page = requests.get(URL, headers=headers) # pylint: disable=W3101
    print(page.status_code)
    soup = BeautifulSoup(page.text, "lxml")
    table = soup.find_all(str(tag), class_ = str(cl))
    return table
