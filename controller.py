'''
This method is a major logic method of my app
'''

import pars
import writer
import reader
import write_chapter
import wordpress_parser

def operations():
    '''
    Menu options
    '''
    option = int(input("1 - pack_links.\n2 - parse_chapters.\n3 - translator.\n"))
    match (option):
        case 1:
            pack_links()
        case 2:
            parse_chapters()

def page(URL):
    '''
    This method takes a link and return the dictionary for json
    '''
    result = pars.parser_(URL)
    links = [{i['title']: i['href']} for i in result]
    return links

def pack_links():
    '''
    1. We get first url from the user.
    2. We are running in cycle to get all links from all pages untill pages is gone out
    3. We put links from each page to json files
    4. We takes links from json file and parse all chapters from the other website
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

def parse_chapters():
    name = input("Name: ")
    lst = reader.read(name)
    for i in lst:
        for key in i:
            val = i[key]
            try:
                text = wordpress_parser.getter_chapter('https:' + val)
                write_chapter.write(text, key)
            except Exception:
                continue

    print("Done, master!")
