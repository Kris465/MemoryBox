'''
This method is a major logic method of my app
'''

import os
import time
import links.pars as pars
import links.writer as writer
import chapters.reader as reader
import translator.txt_writer as txt_writer
import chapters.wordpress_parser as wordpress_parser
from translator.translator import yandex_tr

def operations():
    '''
    Menu options
    '''
    option = int(input("1 - pack_links.\n2 - parse_chapters.\n3 - translate\n"))
    match (option):
        case 1:
            pack_links()
        case 2:
            parse_chapters()
        case 3:
            translate()

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
    '''
    This func parses chapters stepping by links in .json file
    '''
    name = input("Name: ")
    lst = reader.read(name)
    full_lst = []
    for i in lst:
        for key in i:
            val = i[key]
            try:
                text = wordpress_parser.getter_chapter('https:' + val)
                temp_dict = {key: text}
                full_lst.append(temp_dict)
            except Exception:
                continue

    dict_text = {name + "_text": full_lst}
    writer.write(dict_text, name + '_text')

    print("Done, master!")

def translate():
    name = input("Name: ") + "_text"
    chapter = input("Chapter: ")

    lst = reader.read(name)

    for i in lst:
        for key in i:
            if key == chapter:
                val = i[key]
                txt_writer.write(val, name + "_" + key)
                val = val.replace('\n\n', '')
                ch_lst = val.split('\n')
                for elem in ch_lst:
                    tr_chapter = yandex_tr(elem)
                    time.sleep(25)
                    text += tr_chapter
                    print(tr_chapter)
                txt_writer.write(text, name + "_tr_" + key)
            else:
                continue
