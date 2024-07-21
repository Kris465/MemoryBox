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
