# Создание лендинга (html, css, JavaScript)

ADOBE ILLUSTRATOR

Задача 1:  Выберите одну из предложенных тем или используйте свою идею лендинга. Нам понадобятся 2 картинки, одна для фона,  другая для «продукта», который мы «рекламируем». 

Темы:

•	Одежда и аксессуары

•	Геймерские гаджеты и аксессуары

•	Косметика и уход за кожей

•	Спортивные товары и экипировка

•	Книги и журналы

•	Игры и головоломки

•	Товары в онлайн-играх

•	Декор 

Задача 2: Откройте adobe illustrator. Используйте шаблон для веб. Подумайте над подходящими цветами и стилем для будущего лендинга. Одна треть страницы слева будет занята изображением с товаром, поэтому подумайте, что можно было бы поместить на фон, чтобы обыграть рекламный текст и изображение товара. Не ограничивайте свою фантазию. Главное, чтобы основной цвет фона и фона картинки с изображением товара совпадали.

Задача 3: Чтобы графические элементы ровно располагались на холсте, нажмите ctrl + ‘ (Э). Появится сетка. Модульную и колоночную сетку используют для простоты расположения элементов на холсте.

Задача 4: Создайте специальный холст в одну треть по ширине, предыдущего изображения. Создайте изображение «товара» с тем же цветом фона, что и предыдущее изображение.

Задача 5: Подумайте какие цвета текста и шрифты могли бы подойди лендингу.  Если необходимо, разместите текст прямо на картинках. Используйте эффекты.

Задача 6: Экспортируйте оба изображения с форматом png. 

HTML, CSS, JAVASCRIPT

Задача 6: Возьмите шаблон кода. Так он выглядит:
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

Задача 7: Создайте папку, поместите его в папку, переименуйте шаблон из шаблон.txt в index.html. Видоизмените его таким образом, чтобы получилось:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Красивый Лендинг</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="landing-page">
        <div class="product-image"></div>
        <div class="content">
            <h1 class="center">Добро пожаловать на наш лендинг!</h1>
            <p>Описание вашего продукта или услуги здесь.</p>
        </div>

        <div class="feedback-form">
            <div class="circle"></div>
            <div class="form-container">
                <input type="text" placeholder="Имя">
                <input type="email" placeholder="Email">
                <button onclick="submitForm()">Отправить</button>
                <p class="message"></p>
            </div>
        </div>
        
    </div>

    <script src="script.js"></script>
</body>
</html>
```

Задача 8: Замените текст в тегaх: title, h1 + p (заголовок + описание товара или услуги).

Задача 9: Создайте файл со стилями (styles.css), код внутри него будет выглядеть примерно так:

```css
body {
    margin: 0;
    padding: 0;
    font-family: Arial, sans-serif;
    background-image: url('images.jpeg');
    background-size: cover;
}

.landing-page {
    display: flex;
}

.product-image {
    width: 33.33%;
    height: 100vh;
    background-image: url('car.jpg');
    background-size: cover;
    animation: fadeIn 2s ease-in-out; /* Добавляем анимацию появления */
}

@keyframes fadeIn {
    0% {
        opacity: 0;
        transform: scale(0.5);
    }
    100% {
        opacity: 1;
        transform: scale(1);
    }
}

.content {
    width: 66.67%;
    padding: 20px;
}

.center {
    text-align: center;
}

p {
    font-size: 1.2em;
}

.feedback-form {
    position: fixed;
    top: 20px;
    right: 20px;
}

.circle {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    background-color: #333;
    color: #fff;
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;
}

.form-container {
    display: none;
    position: absolute;
    top: 60px;
    left: -220px;
    width: 200px;
    padding: 20px;
    background-color: #f9f9f9;
    border-radius: 5px;
}

.message {
    display: none;
}

button {
    margin-top: 10px;
}
```

Задача 10: Видоизмените цвета, шрифты и названия картинок в соответствии с вашей задумкой. 

Задача 11: Создайте файл script.js и разместите в нем код, для реакции формы обратной связи на нашем лендинге:

```javascript
let timeoutId;

function submitForm() {
    document.querySelector('.message').innerText = 'Мы свяжемся с вами в ближайшее время.';
    document.querySelector('.message').style.display = 'block';
}

document.querySelector('.circle').addEventListener('mouseover', function() {
    clearTimeout(timeoutId); // Очищаем предыдущий таймаут, если он был запущен
    document.querySelector('.form-container').style.display = 'block';
});

document.querySelector('.circle').addEventListener('mouseleave', function() {
    timeoutId = setTimeout(function() {
        document.querySelector('.form-container').style.display = 'none';
    }, 2000); // Задержка в 2 секунды перед скрытием формы
});

document.querySelector('.form-container').addEventListener('mouseover', function() {
    clearTimeout(timeoutId); // Очищаем таймаут, если пользователь навел курсор на форму
});

document.querySelector('.form-container').addEventListener('mouseleave', function() {
    timeoutId = setTimeout(function() {
        document.querySelector('.form-container').style.display = 'none';
    }, 2000); // Задержка в 2 секунды перед скрытием формы
});
```

*Задача 12: Проверьте все и измените код по своему желанию.
