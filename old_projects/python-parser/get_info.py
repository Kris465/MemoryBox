import requests

# URL, к которому вы хотите отправить запрос
url = 'https://example.com'  # Замените на нужный вам URL

# Отправка GET-запроса
response = requests.get(url)

# Получение заголовков ответа
headers = response.headers
print("Заголовки ответа:")
for key, value in headers.items():
    print(f"{key}: {value}")

# Получение куки из ответа
cookies = response.cookies
print("\nКуки:")
for cookie in cookies:
    print(f"{cookie.name}: {cookie.value}")
