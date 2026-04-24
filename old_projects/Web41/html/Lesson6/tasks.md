# Практическое задание:

## Создание собственного сайта:

1. Выберите тему сайта.

2. Подумайте какие страницы вы бы хотели добавить к своему сайту и как они должны выглядеть.

Вот примерная стартовая страница:

```html
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Текст и Картинка</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Добро пожаловать на мой сайт о путешествиях!</h1>
        <nav>
            <ul>
                <li><a href="index.html">Главная</a></li>
                <li><a href="about.html">О проекте</a></li>
                <li><a href="contact.html">Контакты</a></li>
            </ul>
        </nav>
    </header>

    <div class="container">
        <div class="block">
            <div class="text">
                <h2>Заголовок 1</h2>
                <p>Это пример текста для первого блока.</p>
            </div>
            <div class="image">
                <img src="image1.jpg" alt="Пример изображения 1">
            </div>
        </div>
        <div class="block">
            <div class="image">
                <img src="image2.jpeg" alt="Пример изображения 2">
            </div>
            <div class="text">
                <h2>Заголовок 2</h2>
                <p>Это пример текста для второго блока.</p>
            </div>
        </div>
        <div class="block">
            <div class="text">
                <h2>Заголовок 3</h2>
                <p>Это пример текста для третьего блока.</p>
            </div>
            <div class="image">
                <img src="image3.jpeg" alt="Пример изображения 3">
            </div>
        </div>
    </div>

    <footer>
        <p>&copy; 2023 Мой сайт о путешествиях</p>
    </footer>
</body>
</html>
```

Как видите можно сделать ссылку на соседние файлы html, в которых можно написать верстку для других страниц сайта.

3. Далее я приведу примерные блоки, которые вы можете видоизменить через стили и добавить в свой сайт:

- Списки

Списки можно стилизовать с помощью CSS, чтобы они выглядели более привлекательно. Вот пример стилизованного списка:

```css
/* styles.css */
.styled-list {
    list-style-type: none;
    padding: 0;
}

.styled-list li {
    background: #f0f0f0;
    margin: 5px 0;
    padding: 10px;
    border-radius: 5px;
    transition: background 0.3s;
}

.styled-list li:hover {
    background: #e0e0e0;
}
```

Используйте его в HTML:

```html
<ul class="styled-list">
    <li>Первый пункт списка</li>
    <li>Второй пункт списка</li>
    <li>Третий пункт списка</li>
</ul>
```

- Картинки с эффектами

Можно добавить эффекты при наведении на изображения:

```css
/* styles.css */
.image img {
    width: 100%;
    transition: transform 0.3s;
}

.image img:hover {
    transform: scale(1.05);
}
```

- Кнопки

Кнопки можно сделать более привлекательными с помощью стилей:

```css
/* styles.css */
.button {
    background-color: #007bff;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
}

.button:hover {
    background-color: #0056b3;
}
```

Используйте кнопку в HTML:

```html
<button class="button">Нажми меня</button>
```

- Карточки

Карточки — отличный способ организовать информацию визуально:

```css
/* styles.css */
.card {
    border: 1px solid #ddd;
    border-radius: 5px;
    padding: 15px;
    margin: 10px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

.card img {
    max-width: 100%;
    border-radius: 5px;
}
```

```html
<div class="card">
    <img src="image.jpg" alt="Пример изображения">
    <h3>Заголовок карточки</h3>
    <p>Некоторый текст о содержимом карточки.</p>
</div>
```

- Модальное окно

Модальные окна могут быть полезны для отображения дополнительной информации без перехода на другую страницу.

HTML для модального окна:

```html
<!-- Кнопка для открытия модального окна -->
<button id="openModal" class="button">Открыть модальное окно</button>

<!-- Модальное окно -->
<div id="myModal" class="modal">
    <div class="modal-content">
        <span class="close">&times;</span>
        <h2>Заголовок модального окна</h2>
        <p>Некоторый текст внутри модального окна.</p>
    </div>
</div>
```

```css
/* styles.css */
.modal {
    display: none; /* Скрыто по умолчанию */
    position: fixed; /* Остается на месте */
    z-index: 1; /* На переднем плане */
    left: 0;
    top: 0;
    width: 100%; /* Ширина полная */
    height: 100%; /* Высота полная */
    overflow: auto; /* Включает прокрутку при необходимости */
    background-color: rgb(0,0,0); /* Черный фон с прозрачностью */
    background-color: rgba(0,0,0,0.4); /* Черный фон с прозрачностью */
}

.modal-content {
    background-color: #fefefe;
    margin: 15% auto; /* 15% сверху и центрирование */
    padding: 20px;
    border: 1px solid #888;
    width: 80%; /* Ширина */
}

.close {
    color: #aaa;
    float: right;
    font-size: 28px;
    font-weight: bold;
}

.close:hover,
.close:focus {
    color: black;
    text-decoration: none;
    cursor: pointer;
}
```
JavaScript для управления модальным окном:

```js
// script.js
var modal = document.getElementById("myModal");
var btn = document.getElementById("openModal");
var span = document.getElementsByClassName("close")[0];

btn.onclick = function() {
    modal.style.display = "block";
}

span.onclick = function() {
    modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

```
