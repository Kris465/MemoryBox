source passwords.cfg

URL="https://tl.rulate.ru"
login=$login
password=$password

response=$(curl -s -o /dev/null -w "%{http_code}" -X POST -d "username=$USERNAME&password=$PASSWORD" -H "Content-Type: application/json" -H "Accept: application/json" $URL)

if [ $response -eq 200 ]; then
    echo "Аутентификация прошла успешно (HTTP статус код: $response)"
else
    echo "Ошибка аутентификации (HTTP статус код: $response)"
fi
