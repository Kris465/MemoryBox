#!/bin/bash

source passwords.cfg

url="https://tl.rulate.ru/book/95179"
login=$login
password=$password

response=$(curl -c cookies.txt -X POST -d "login=$login&password=$password" -H "Content-Type: application/json" -H "Accept: application/json" $url)

echo $response > output.html
