import requests
from bs4 import BeautifulSoup

from writer_to_txt import write_txt

url = 'https://www.52shuwu.me/chongsheng/56400_2.html'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                           AppleWebKit/537.36 (KHTML, like Gecko)\
                           Chrome/111.0.0.0 Safari/537.36'}
response = requests.get(url, headers=headers)
response.encoding = response.apparent_encoding
new_text = response.text
soup = BeautifulSoup(response.text, 'html.parser')

# write_txt("test1", new_text)

text = soup.find('div', 'article-content')
write_txt("test", text.text)
