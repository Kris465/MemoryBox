import os
from dotenv import load_dotenv, find_dotenv
import re
from parser_module import parser_
from writer_to_json import write


def options():
    option = int(input("1 - parse\n2 - translate\n"))

    match (option):
        case 1:
            parse()
        case 2:
            translate()
    

def parse():
    '''
    name: {ch: {link: text}}
    '''
    title = input("title: ")
    URL = input("URL: ")
    pages = parser_(URL, 'div', 'digg_pagination')
    cycle_flag = False
    full_dict = {}

    for elem in pages:
        result = re.findall(r'\d+', elem.text)
        print(result[-1])
        cycle_flag = True

    if cycle_flag:
        URL = URL + '?pg=1#myTable'
        for i in range(int(result[-1])):
            links = page(URL, 'a', 'chp-release')
            full_dict.update(links)
            URL = URL[0:-9] + str(i + 2) + "#myTable"
    else:
        full_dict = page(URL, 'a', 'chp-release')
    
    write(full_dict, title)


def page(URL, tag, cl):
    result = parser_(URL, tag, cl)
    links = {i['title']: i['href'] for i in result}
    return links

# URL = read(title) хочу использовать для проверки обновлений. Надо по названию брать ссылку на проект из списка и проверять, есть ли новые главы.
    
def translate():
    pass
