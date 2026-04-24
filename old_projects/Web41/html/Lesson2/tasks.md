# Второй урок HTML верстки. Работа с текстом с помощью HTML + CSS

## Как можно работать с тексом с помощью html.

▎Основные элементы HTML для работы с текстом

1. Заголовки: 
```html
    - <h1> - <h6>: Заголовки, где <h1> — самый важный, а <h6> — наименее важный.
```
2. Параграфы:
```html
   - <p>: Для обычного текста.
```

3. Форматирование текста:
```html
   - <strong>: Для выделения важного текста (обычно жирным).
   - <em>: Для выделения (обычно курсивом).
   - <b>: Для жирного текста без семантического значения.
   - <i>: Для курсивного текста без семантического значения.
   - <u>: Для подчеркивания текста.
   - <mark>: Для выделения текста (обычно фоновым цветом).
   - <small>: Для меньшего текста.
   - <del>: Для зачеркивания текста.
   - <ins>: Для вставленного текста.
```

4. Списки:
```html
   - Ненумерованные списки: <ul> с элементами <li>.
   - Нумерованные списки: <ol> с элементами <li>.
```

5. Цитаты:
```html
   - <blockquote>: Для длинных цитат.
   - <q>: Для коротких цитат.
```

6. Ссылки:
```html
   - <a href="">: Для создания гиперссылок.
```

7. Изображения:
```html
   - <img src="" alt="">: Для вставки изображений, которые могут сопровождать текст.
```

8. Таблицы:
```html
   - <table>, <tr>, <td>, <th>: Для представления данных в табличном формате.
```

▎Основные стили CSS для работы с текстом

1. Цвет и фон:

   - color: Установка цвета текста.
   - background-color: Установка фона элемента.

2. Шрифты:
   - font-family: Установка шрифта.
   - font-size: Установка размера шрифта.
   - font-weight: Установка толщины шрифта (normal, bold и т.д.).
   - font-style: Установка стиля шрифта (normal, italic, oblique).

3. Выравнивание:
   - text-align: Установка выравнивания текста (left, right, center, justify).

4. Отступы и поля:
   - margin: Внешние отступы.
   - padding: Внутренние отступы.

5. Линии и высота:
   - line-height: Высота строки.
   - text-decoration: Подчеркивание, зачеркивание и т.д.

6. Текстовые эффекты:
   - text-transform: Преобразование регистра (uppercase, lowercase, capitalize).
   - letter-spacing: Интервал между буквами.
   - word-spacing: Интервал между словами.


### Больше можно почитать:
https://htmlbook.ru/samhtml/vvedenie-v-html

https://www.w3schools.com/css/css_syntax.asp

### Задача 1: 

Давайте попробуем решить эти задачи: https://htmlbook.ru/practical/theme/tekst

И на этих примерах освоимся с основами верстки. 

### Задача 2:

Попробуйте создать интерфейс сайта - читалки. Шаблон для его создания:

    index.html : 

```html
   <!DOCTYPE html>
   <html lang="ru">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>Сайт-Читалка</title>
       <link rel="stylesheet" href="styles.css">
   </head>
   <body>
       <header>
           <h1>Моя Читалка</h1>
       </header>
       <main>
           <article>
               <h2>Заголовок статьи</h2>
               <p>Это пример текста статьи.</p>
               <p><strong>Выделенный текст</strong> и <em>курсивный текст</em>.</p>
           </article>
       </main>
       <footer>
           <p>&copy; 2023 Моя Читалка</p>
       </footer>
   </body>
   </html>
   
```
    styles.css :

```css
   body {
       font-family: Arial, sans-serif;
       line-height: 1.6;
       margin: 0;
       padding: 0;
       background-color: #f4f4f4;
   }
   
   header {
       background: #333;
       color: #fff;
       padding: 10px 0;
       text-align: center;
   }
   
   main {
       padding: 20px;
       max-width: 800px;
       margin: auto;
       background: #fff;
       box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
   }
   
   footer {
       text-align: center;
       padding: 10px 0;
       background: #333;
       color: #fff;
       position: relative;
       bottom: 0;
       width: 100%;
   }
   
```

### Задача 3:
Выберите то задание из дз, которое вы еще не делали и выполните его. Файлы с кодом необходимо сшить в архив и приложить в journal
