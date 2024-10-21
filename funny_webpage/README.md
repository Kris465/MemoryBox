# Страница про любимого персонажа

Задача 1: Копируйте из общей папки шаблон кода. Переименуйте его в index.html. В эту же папку поместите изображение с любимым персонажем. Шаблон выглядит так:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Заголовок страницы</title>
</head>
<body>
    <header>
        <h1>Заголовок страницы</h1>
    </header>

    <div> …
    </div>
</body>
</html>
```

Задача 2:  В теге title, укажите заголовок страницы:

```html
 <title>Мой любимый персонаж</title>
```

Задача 3: На следующей строчке, конечно же, добавьте строку со ссылкой на css стили:

```html
 <link rel="stylesheet" href="styles.css">
```

Задача 4: Создайте файл styles.css 

Задача 5: В теге h1 напишите «Мой любимый персонаж». Должно получиться так:

```html
<h1>Мой любимый персонаж</h1>
```

Задача 6: На следующей строке, с тем же отступом, что из заголовок, вставьте ссылку на картинку, в html, это выглядит так:

```html
<img src="hero.jpg" alt="Постер с любимым персонажем">
```

Задача 7: Вставьте под картинкой текст с помощью тега p (абзац),  с тем же отступом, что предыдущая строка:

```html
<p id="description">Описание персонажа</p>
```

Задача 8: Создайте кнопку с помощью тега button и разместите ниже, с тем же отступом:

```html
<button onclick="changeDescription()">Изменить описание</button>
```

Задача 9:  Создайте файл script.js и разместите для него в index.html тег, как раз под кнопкой, с тем же отступом:

```html
<script src="script.js"></script>
```

Задача 10: Откройте файл со стилями (styles.css) и задайте цвет для заголовка:

```css
h1 {
    color: #333;
}
```

Задача 11: Там же, в файле со сталями, создайте свойства для тега body (фон, шрифт, расположение): 

```css
body {
    font-family: Arial, sans-serif;
    text-align: center;
    background-color: #f0f0f0;
}
```

Задача 11: Задайте стиль для картинки:

```css
img {
    max-width: 100%;
    border: 2px solid #333;
    border-radius: 10px;
}
```

Задача 12: И для кнопки:

```css
button {
    padding: 10px 20px;
    background-color: #007bff;
    color: white;
    border: none;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}
```

Задача 13: Откройте файл script.js и создайте функцию, обрабатывающую поведение кнопки:

```javascript
function changeDescription() {
    var description = prompt("Введите новое описание персонажа:");
    if (description !== null) {
        document.getElementById("description").textContent = description;
    }
}
```

*Задача 14: Подумайте и измените какие пожелаете характеристики, чтобы улучшить веб-страницу. Не бойтесь проявлять креатив и пользоваться поисковиком и документацией. 
