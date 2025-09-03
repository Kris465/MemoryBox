# Отбей квадратик

Задача 1: Возьмите шаблон кода, поместите его в новую папку и откройте в vs code. Переименуйте в Index.html. Примерно так он выглядит:

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

Задача 2: Создайте структуру игры в файле index.html:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Survive!</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="game-area">
        <div class="paddle"></div>
        <div class="ball"></div>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

Задача 3: Создайте файл styles.css и поместите в него стили для игры:

```css
body {
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-color: #f0f0f0;
}

.game-area {
    position: relative;
    width: 600px;
    height: 400px;
    background-color: #333;
}

.paddle {
    position: absolute;
    bottom: 10px;
    width: 80px;
    height: 10px;
    background-color: #fff;
}

.ball {
    position: absolute;
    width: 10px;
    height: 10px;
    background-color: #fff;
}

```

Задача 3: Создайте файл script.js и поместите туда логику игры:

```javascript
const paddle = document.querySelector('.paddle');
const ball = document.querySelector('.ball');

let ballX = 250;
let ballY = 350;
let ballDX = 2;
let ballDY = -2;

let paddleX = 225;

function movePaddle(e) {
    if (e.key === 'ArrowLeft' && paddleX > 0) {
        paddleX -= 20;
    } else if (e.key === 'ArrowRight' && paddleX < 480) {
        paddleX += 20;
    }

    paddle.style.left = paddleX + 'px';
}

function moveBall() {
    ballX += ballDX;
    ballY += ballDY;
    
    if (ballX + ball.clientWidth >= 600 || ballX <= 0) {
        ballDX = -ballDX;
    }

    if (ballY <= 0) {
        ballDY = -ballDY;
    }

    if (ballY + ball.clientHeight >= 400) {
        alert("Game Over!");
    }

    if (ballY + ball.clientHeight >= paddle.offsetTop && 
        ballX + ball.clientWidth >= paddle.offsetLeft && 
        ballX <= paddle.offsetLeft + paddle.clientWidth) {
        ballDY = -ballDY;
    }

    ball.style.left = ballX + 'px';
    ball.style.top = ballY + 'px';
}

document.addEventListener('keydown', movePaddle);

function startGame() {
    setInterval(moveBall, 10);
}

startGame();
```

Задача 5: Попробуйте видоизменить внешний облик игры. 

*Задача 6: Попробуйте найти баг в игре и исправить его.
