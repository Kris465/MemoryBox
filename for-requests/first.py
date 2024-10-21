import requests

url = "https://tl.rulate.ru/book/95179"
page = requests.get(url)
with open("output.html", "w", encoding='utf-8') as file:
    file.write(page.text)
