import requests
from bs4 import BeautifulSoup

url = 'https://www.52shuku.vip/yanqing/hyv3.html'

response = requests.get(url)

if response.status_code == 200:
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, 'html.parser')
    
    result = soup.find_all()
    print(result)
else:
    print(f"Some troubles: {response.status_code}")
