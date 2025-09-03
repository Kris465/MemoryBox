'''
My tries of making parser. Try number 1

'''
from bs4 import BeautifulSoup
import requests

URL="https://cabinfourtranslations.wordpress.com/2022/07/15/sss-grade-cafe-in-front-of-the-dungeon-chapter-1/"
page = requests.get(URL)
print(page.status_code)
needed_text = []

soup = BeautifulSoup(page.text, "lxml")
print(soup.find_all("p"))
# by chance it was partly succeed... Sometimes I think that I'm the silliest of people...
