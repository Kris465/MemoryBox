import requests
from bs4 import BeautifulSoup


url = "https://www.crimsonnovels.com/searchbook"
response = requests.get(url)
print(response.status_code)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find('h2')
    print(title)
else:
    print("Ошибка!")
