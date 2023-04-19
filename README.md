# Parser

Я разделила проект на два репозитория, потому что части расчитаны на разных пользователей. 

## Функционал проекта:

**Парсер:**

1. Сбор ссылок с сайта по новелле (https://www.novelupdates.com/)

2. Сбор и запись глав по собранным ссылкам.

3. Перевод глав.

4. Запись оригинальных глав и переведенных в бд.

## Сбор ссылок. 

Код по этому функционалу находится в директории links.

## Сбор глав.

Код по этому функционалу находится в директории chapters.

## Перевод глав.

Код по этому функционалу находится в директории translator.

## Запись глав в бд. 

Этот функционал пока не реализован.

## Общая информация о проекте.

1. Точка входа в приложение - модуль main.py

2. Ключей в коде нет, так что имеет смысл сначала достать свои ключи, а потом уже запускать проект. (Ключи спрятаны с помощью библиотеки dotenv, поэтому конфигурационный файл не пушится в репозиторий)

3. Проект рассчитан на работу по шаблону, но один раз с одним воспроизведением. (Поэтому перед запуском необходимо изучить новеллу: получить нужный формат ссылки с новелапдейтс (со страницей таблицы), посмотреть на домен глав (вордперсс или нет), открыть инструменты разработчика и сверить теги, уточнить каких именно глав нужен перевод (проект реализован на api яндекс-переводчика а там идет посимвольная оплата))

![Иллюстрация к проекту](https://github.com/Kris465/Pars/blob/main/diagram.puml)
