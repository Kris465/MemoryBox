import requests
from bs4 import BeautifulSoup

url = 'https://www.xbanxia.com/books/109819/23141778.html'

response = requests.get(url)

if response.status_code == 200:
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, 'html.parser')

    result = soup.text
    print(result)
else:
    print(f"Some troubles: {response.status_code}")
