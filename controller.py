'''
This method is a major logic method of my app
'''

import pars
import writer
import reader
import write_chapter
import wordpress_parser

def operations():
    option = int(input("1 - pack_links.\n2 - parse_chapters.\n"))
    match (option):
        case 1:
            pack_links()
        case 2:
            parse_chapters()

def page(URL):
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
        val = i.values()
        key = i.keys()
        text = wordpress_parser.getter_chapter(val)
        write_chapter.write(text, key)

    print("Done, master!")
