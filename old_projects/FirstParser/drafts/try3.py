'''
One more try to make a parser
'''

import requests
from bs4 import BeautifulSoup

def get_html(url):
    '''
    this funtion gets html
    '''
    result = requests.get(url)
    return result.text

def get_data(html):
    '''
    this function gets data from html
    '''
    soup = BeautifulSoup(html, 'lxml')

def main():
    '''
    This is the main function
    '''
    html = get_html('"https://cabinfourtranslations.wordpress.com/"')
    print(html)

if __name__ == '__main__':
    main()
