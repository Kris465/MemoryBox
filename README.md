# Змейка

Задача 1: Создайте папку, поместите туда шаблон кода. Откройте ее в vs code. Шаблон выглядит так:

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

Задача 2: В файле index.html создайте структуру игры:

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Змейка</title>
<link rel="stylesheet" href="styles.css">
</head>
<body>
<div class="game-area"></div>
<script src="script.js"></script>
</body>
</html>
```

Задача 3: Создайте файл styles.css и напишите стили для игры:

```css
body {
    margin: 0;
    overflow: hidden;
}

.game-area {
    width: 100vw;
    height: 100vh;
    background-color: #fbfbfb;
    position: relative;
}

.snake {
    width: 10px;
    height: 10px;
    background-color: green;
    position: absolute;
}

.food {
    width: 10px;
    height: 10px;
    background-color: red;
    position: absolute;
}
```

Задача 4: Создайте файл script.js и создайте логику игры:

```javascript
const gameArea = document.querySelector('.game-area');
let snake = [{x: 10, y: 10}];
let food = {x: 200, y: 200};
let direction = 'right';
let gameInterval;

function draw() {
    gameArea.innerHTML = '';
    
    snake.forEach(segment => {
        const snakeElement = document.createElement('div');
        snakeElement.style.left = segment.x + 'px';
        snakeElement.style.top = segment.y + 'px';
        snakeElement.classList.add('snake');
        gameArea.appendChild(snakeElement);
    });

    const foodElement = document.createElement('div');
    foodElement.style.left = food.x + 'px';
    foodElement.style.top = food.y + 'px';
    foodElement.classList.add('food');
    gameArea.appendChild(foodElement);
}

function update() {
    const head = {x: snake[0].x, y: snake[0].y};

    if (direction === 'right') head.x += 10;
    if (direction === 'left') head.x -= 10;
    if (direction === 'up') head.y -= 10;
    if (direction === 'down') head.y += 10;

    if (head.x < 0 || head.x >= window.innerWidth || head.y < 0 || head.y >= window.innerHeight) {
        clearInterval(gameInterval);
        alert('Игра окончена! Столкновение со стеной.');
        return;
    }

    snake.unshift(head);

    if (head.x === food.x && head.y === food.y) {
        food.x = Math.floor(Math.random() * window.innerWidth / 10) * 10;
        food.y = Math.floor(Math.random() * window.innerHeight / 10) * 10;
    } else {
        snake.pop();
    }
}

function gameLoop() {
    update();
    draw();
}

document.addEventListener('keydown', (event) => {
    if (event.key === 'ArrowRight' && direction !== 'left') {
        direction = 'right';
    } else if (event.key === 'ArrowLeft' && direction !== 'right') {
        direction = 'left';
    } else if (event.key === 'ArrowUp' && direction !== 'down') {
        direction = 'up';
    } else if (event.key === 'ArrowDown' && direction !== 'up') {
        direction = 'down';
    }
});

gameInterval = setInterval(gameLoop, 100);
```

Задача 5: Молодцы! Создали игру! А теперь… В файле со стилями измените фон на тот, который вам хочется и сделайте змейку и еду больше по размерам. 

Задача 6: Придайте игре уникальные свойства, используя свойства стилей:

1. background-color - цвет фона элемента
2. background-image - изображение фона элемента
3. background-size - размер изображения фона
4. background-position - позиция фона
5. border - стиль, ширина и цвет границы элемента
6. border-radius - скругление углов элемента
7. box-shadow - тень элемента
8. color - цвет
9. font-family - семейство шрифтов
10. font-size - размер шрифта
11. text-align - выравнивание текста
12. text-decoration - стиль текста
13. line-height - высота строки
14. padding - отступы внутри элемента
15. margin - внешние отступы элемента
16. width - ширина элемента
17. height - высота элемента
18. position - позиционирование элемента
19. transform - трансформация элемента (поворот, масштабирование и т. д.)
20. animation - создание анимации
21. transition - добавление плавных переходов
22. filter - применение фильтров к изображениям (например, размытие)
23. opacity - прозрачность элемента
24. cursor - стиль курсора при наведении на элемент
25. overflow - обработка переполнения контента
26. z-index - порядок слоев элементов
27. clip-path - обрезка элемента по заданной области
28. grid-template-columns - определение ширины колонок в сетке
29. grid-template-rows - определение высоты строк в сетке
30. perspective и transform-style: preserve-3d - создание трехмерного эффекта
