#!/bin/bash

# URL для отправки POST-запроса
url="https://tl.rulate.ru/register"

# Данные для авторизации (пример)
username="your_username"
password="your_password"

# Отправляем POST-запрос для авторизации и сохраняем ответ в переменной response
response=$(curl -s -X POST -d "username=$username&password=$password" $url)

# Печатаем HTML-ответ
echo "$response" > output.html

# Выводим HTML-ответ в консоль
echo "$response"
