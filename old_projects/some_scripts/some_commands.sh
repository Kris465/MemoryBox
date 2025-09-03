#!/bin/bash

# Чтение логина и пароля из файла
credentials=$(<credentials.txt)

# URL для авторизации
login_url="https://tl.rulate.ru/register/settings"

# URL для выполнения действий в ЛК
# actions_url="https://example.com/actions"

# Авторизация
login_response=$(curl -s -X POST -d "$credentials" $login_url)

# Проверка успешной авторизации
if [[ $login_response == *"Успешно"* ]]; then
    echo "Авторизация прошла успешно"
    
    # Выполнение действий в ЛК
    actions_response=$(curl -s $actions_url)
    
    # Обработка результатов действий
    echo "Результаты действий: $actions_response"
else
    echo "Ошибка авторизации"
fi
