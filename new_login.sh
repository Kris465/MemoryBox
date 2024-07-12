#!/bin/bash

# Указываем URL для авторизации и получения страницы
login_url="https://tl.rulate.ru/"
dashboard_url="https://tl.rulate.ru/register/settings"

# Читаем логин и пароль из файла credentials.txt
readarray -t credentials < credentials.txt
username="${credentials[0]}"
password="${credentials[1]}"

# Определяем заголовки
headers="User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
# Другие заголовки можно добавить по аналогии

# Отправляем POST-запрос для авторизации и сохраняем куки в файл
curl -c cookies.txt -d "username=$username&password=$password" -H "$headers" $login_url

# Отправляем GET-запрос для получения страницы после авторизации
response=$(curl -b cookies.txt -L -H "$headers" $dashboard_url)

# Печатаем HTML-ответ
echo "$response" > output.html
