'''
This method is a major logic method of my app
'''

import pars
import writer

def operations():
    '''
    1. We get first url from the user.
    2. We are running in cycle to get all links from all pages untill pages is gone out
    3. We put links from each page to json files
    '''

    URL = input("URL: ")
    pages = int(input("Pages: "))
    full_lst = []
    number = 1
    while number <= pages:
        URL = URL[0:-9] + str(number) + "#myTable"
        lst = page(URL)
        full_lst.extend(lst)
        number += 1

    name = input("Name of progect: ")
    dict_links = {name: full_lst}
    writer.write(dict_links, name)

def page(URL):
    result = pars.parser_(URL)
    links = [{i['title']: i['href']} for i in result]
    return links
