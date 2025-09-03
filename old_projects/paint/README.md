# Упрощенный Paint

Задача 1: Создайте новую папку и поместите в нее картинку для заднего фона и шаблон кода из общей папки. Он выглядит примерно так:

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

Задача 2: Переименуйте файл в index.html и напишите каркас упрощенного paint:

```html
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Упрощенный Paint</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="menu">
        <label for="color">Цвет:</label>
        <input type="color" id="color" value="#000000">

        <label for="brushSize">Размер кисти:</label>
        <input type="range" id="brushSize" min="1" max="100" value="5">

        <button id="pencil">Карандаш</button>
        <button id="squareOutline">Контур квадрата</button>
        <button id="circleOutline">Контур круга</button>
        <button id="filledSquare">Залитый квадрат</button>
        <button id="filledCircle">Залитый круг</button>
        <button id="eraser">Ластик</button>
        <button id="save">Сохранить</button> <!-- Кнопка сохранения -->
    </div>

    <canvas id="canvas"></canvas>

    <script src="script.js"></script>
</body>
</html>
```

Задача 3: Создайте файл styles.css и напишите его код:

```css
body {
    margin: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    background-image: url('Background.png');
    background-size: cover;
}

.menu {
    background-color: rgba(255, 255, 255, 0.8);
    padding: 10px;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
    margin-bottom: 10px;
    display: flex;
    gap: 10px;
}

canvas {
    border: 1px solid #ccc;
    background-color: white;
    cursor: crosshair;
}
```

Задача 4: Создайте файл script.js и напишите логику paint:

```javascript
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');

canvas.width = window.innerWidth - 20;
canvas.height = window.innerHeight - 100;

let painting = false;
let currentTool = 'pencil';
let brushColor = '#000000';
let brushSize = 5;
let startX, startY; // Начальные координаты для фигур

function startPosition(e) {
    painting = true;
    startX = e.clientX - canvas.offsetLeft;
    startY = e.clientY - canvas.offsetTop;
    draw(e); // Если это карандаш, сразу начинаем рисовать
}

function endPosition() {
    if (currentTool !== 'pencil') {
        drawShape(); // Рисуем фигуру при отпускании мыши
    }
    painting = false;
    ctx.beginPath();
}

function draw(e) {
    if (!painting || currentTool === 'squareOutline' || currentTool === 'circleOutline' || currentTool === 'filledSquare' || currentTool === 'filledCircle') return;

    ctx.lineWidth = brushSize;
    ctx.lineCap = 'round';
    ctx.strokeStyle = brushColor;

    ctx.lineTo(e.clientX - canvas.offsetLeft, e.clientY - canvas.offsetTop);
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(e.clientX - canvas.offsetLeft, e.clientY - canvas.offsetTop);
}

// Функция для рисования фигуры
function drawShape() {
    const width = 100; // Ширина фигуры (можно сделать динамической)
    const height = 100; // Высота фигуры (можно сделать динамической)
    
    ctx.fillStyle = brushColor;
    ctx.strokeStyle = brushColor;

    switch (currentTool) {
        case 'squareOutline':
            ctx.strokeRect(startX, startY, width, height);
            break;
        case 'circleOutline':
            ctx.beginPath();
            ctx.arc(startX + width / 2, startY + height / 2, width / 2, 0, Math.PI * 2);
            ctx.stroke();
            break;
        case 'filledSquare':
            ctx.fillRect(startX, startY, width, height);
            break;
        case 'filledCircle':
            ctx.beginPath();
            ctx.arc(startX + width / 2, startY + height / 2, width / 2, 0, Math.PI * 2);
            ctx.fill();
            break;
        default:
            break;
    }
}

// Устанавливаем события мыши
canvas.addEventListener('mousedown', startPosition);
canvas.addEventListener('mouseup', endPosition);
canvas.addEventListener('mousemove', draw);

// Обработчики для инструментов
document.getElementById('color').addEventListener('input', (e) => {
    brushColor = e.target.value;
});

document.getElementById('brushSize').addEventListener('input', (e) => {
    brushSize = e.target.value;
});

document.getElementById('pencil').addEventListener('click', () => {
    currentTool = 'pencil';
});

document.getElementById('eraser').addEventListener('click', () => {
    currentTool = 'eraser';
    brushColor = '#FFFFFF';
});

// Обработчики для фигур
document.getElementById('squareOutline').addEventListener('click', () => {
    currentTool = 'squareOutline';
});

document.getElementById('circleOutline').addEventListener('click', () => {
    currentTool = 'circleOutline';
});

document.getElementById('filledSquare').addEventListener('click', () => {
    currentTool = 'filledSquare';
});

document.getElementById('filledCircle').addEventListener('click', () => {
    currentTool = 'filledCircle';
});

// Сохранение изображения
document.getElementById('save').addEventListener('click', () => {
    const link = document.createElement('a');
    link.download = 'drawing.png';
    link.href = canvas.toDataURL();
    link.click();
});
```