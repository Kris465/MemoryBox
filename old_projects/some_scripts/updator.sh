#!/bin/bash

source passwords.cfg

url="https://tl.rulate.ru"
login=$login
password=$password

response= curl -X POST $url \
     -H "Content-Type: application/json" \
     -d "{\"username\": \"$username\", \"password\": \"$password\"}" \
     -c cookies.txt

main_link="https://tl.rulate.ru/book/95179"
webpage= curl -X GET $main_link -d "cookies.txt"
book_number=$(echo "$main_link" | grep -o '[0-9]*$')

all_links=$(echo "$webpage" | grep -o '<a [^>]*href="[^"]*"' | grep -o 'href="[^"]*"' | cut -d'"' -f2)

matching_links=""

for link in $all_links; do
    if echo "$link" | grep -q "/book/$book_number"; then
        matching_links="$matching_links $link"
    fi
done

if [ -n "$matching_links" ]; then
    echo "Ссылки на странице с номером книги $book_number:"
    echo "$matching_links"
    echo "$matching_links" > output.txt
else
    echo "Ссылки с номером книги $book_number не найдены"
fi
