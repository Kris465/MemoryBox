import requests


def get_status_code(url):
    try:
        response = requests.get(url)
        return response.status_code
    except requests.exeptions.RequestExeption as e:
        return f"Ошибка: {e}"


def main():
    url = input("Введите адрес веб- сайта: ")
    status_code = get_status_code(url)
    print(f'Статус код для {url}: {status_code}')


main()
