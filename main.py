import requests

url = 'https://tl.rulate.ru/'
response = requests.get(url)
if response.ok:
    with open('page.html', 'w', encoding='utf-8') as file:
        file.write(response.text)
    print("Файл сохранен")
else:
    print("Не удалось получить код страницы")
