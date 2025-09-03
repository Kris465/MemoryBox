from bs4 import BeautifulSoup
import requests

URL="https://cabinfourtranslations.wordpress.com/2022/07/15/sss-grade-cafe-in-front-of-the-dungeon-chapter-1/"
page = requests.get(URL)
print(page.status_code)
needed_text = []

soup = BeautifulSoup(page.text, "lxml")
print(soup)
