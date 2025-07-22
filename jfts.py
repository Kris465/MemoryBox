import requests
from bs4 import BeautifulSoup
from tools.file_manager import read_from_json
from tools.other_tools import get_domain_name


def test_selector(url):
    domain = get_domain_name(url)
    selectors_config = read_from_json("selectors.json")
    selector = selectors_config[domain]['selector']
    session = requests.Session()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
    }

    response = session.get(url, headers=headers)
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, 'html.parser')
    link_element = soup.select_one(selector)

    if link_element and link_element.has_attr('href'):
        extracted_link = link_element['href']
        print(f"Успешно извлечена ссылка: {extracted_link}")
        return extracted_link
    else:
        print("Не удалось извлечь ссылку по указанному селектору")
        return None


if __name__ == '__main__':
    test_url = "https://moonlightnovel.com/the-ex-wife-of-the-educated-youth-is-reborn/teweyr-c1/"
    result = test_selector(test_url)
    print(f"Результат: {result}")
