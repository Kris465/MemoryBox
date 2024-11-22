import requests


def main():
    url = 'https://tl.rulate.ru/book/16292/327323/ready_new'
    response = requests.get(url)
    print(response.status_code)

    with open("output.html", "a", encoding="UTF-8") as file:
        file.write(response.text)


if __name__ == '__main__':
    main()
