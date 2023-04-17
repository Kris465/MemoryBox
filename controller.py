import os
from dotenv import load_dotenv, find_dotenv
from get_url import read
from parser_novelupdates import parser_


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
    answer = parser_(URL, 'div', 'digg_pagination')
    print(answer)



    # try:
    #     if '#myTable' in URL:
    #         temp_url = URL
    #     else:
    #         temp_url = URL + "?pg=" + str(number) + "#myTable"

    #     while lst is not None:
    #         lst = page(temp_url)
    #         full_lst.extend(lst)
    #         temp_url = URL[0:-9] + str(number) + "#myTable"
    #         number += 1
    #     return number

    # except Exception:
    #     return page(URL)

# def page(URL):
#     result = parser_(URL)
#     links = [{i['title']: i['href']} for i in result]
#     return links

# URL = read(title) хочу использовать для проверки обновлений. Надо по названию брать ссылку на проект из списка и проверять, есть ли новые главы.

def get_link(title):
    pass
    
def translate():
    pass
