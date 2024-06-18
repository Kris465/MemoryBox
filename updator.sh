#!/bin/bash

source passwords.cfg

url="https://tl.rulate.ru/book/95179"
login=$login
password=$password

response=$(curl -s -X POST -d "login=$login&password=$password" -b "cookies.txt" $url)

echo $response > output.html

# if [[ $response == *"Welcome"* ]]; then
#     echo "Успешно залогинились!"
# else
#     echo "Не удалось залогиниться. Проверьте данные для входа."
# fi

# main_link="https://tl.rulate.ru/book/95179"
# book_number=$(echo "$main_link" | grep -o '[0-9]*$')

# all_links=$(echo "$response" | grep -o '<a [^>]*href="[^"]*"' | grep -o 'href="[^"]*"' | cut -d'"' -f2)

# matching_links=""

# for link in $all_links; do
#     if echo "$link" | grep -q "/book/$book_number"; then
#         matching_links="$matching_links $link"
#     fi
# done

# if [ -n "$matching_links" ]; then
#     echo "Ссылки на странице с номером книги $book_number:"
#     echo "$matching_links"
#     echo "$matching_links" > output.txt
# else
#     echo "Ссылки с номером книги $book_number не найдены"
# fi

