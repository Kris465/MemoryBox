source passwords.cfg

url="https://tl.rulate.ru/book/95179"
login=$login
password=$password

response=$(curl -s -o /dev/null -w "%{http_code}" -c cookies.txt -X POST -d "login=$login&password=$password" -H "Content-Type: application/json" -H "Accept: application/json" $url)

if [ $response -eq 200 ]; then
    echo "Аутентификация прошла успешно (HTTP статус код: $response)"
    curl -b cookies.txt $url > output.html
else
    echo "Ошибка аутентификации (HTTP статус код: $response)"
fi
