import requests
from bs4 import BeautifulSoup

url = 'https://www.52shuku.vip/yanqing/hyv3.html'

response = requests.get(url)

if response.status_code == 200:
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, 'html.parser')
    soup = soup.find("ul", class_="list clearfix")
    elements = soup.find_all("a")
    links = []
    for element in elements:
        href = element.get('href')
        if href:
            links.append(href)
    print(links)
else:
    print(f"Some troubles: {response.status_code}")
