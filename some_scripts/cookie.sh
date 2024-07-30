#!/bin/bash

source passwords.cfg
url="https://tl.rulate.ru/book/95179"
login=$login
password=$password

curl -c cookies.txt $url
