let score = 0;
let timeLeft = 30;
let gameInterval;
let timerInterval;

const mouse = document.getElementById('mouse');
const scoreDisplay = document.getElementById('score');
const timerDisplay = document.getElementById('timer');
const startBtn = document.getElementById('start-btn')

function moveMouse() {
    const gameArea = document.querySelector('.game-area');
    const maxX = gameArea.clientWidth - mouse.clientWidth;
    const maxY = gameArea.clientHeight - mouse.clientHeight;

    const randomX = Math.floor(Math.random() * maxX);
    const randomY = Math.floor(Math.random() * maxY);
    
    mouse.style.left = `${randomX}px`;
    mouse.style.top = `${randomY}px`;
}

function startGame() {
    score = 0;
    timeLeft = 30;
    scoreDisplay.textContent = score;
    timerDisplay.textContent = timeLeft;

    moveMouse();

    gameInterval = setInterval(() => {
        timeLeft--;
        timerDisplay.textContent = timeLeft;

        if (timeLeft <= 0) {
            clearInterval(gameInterval);
            clearInterval(timerInterval);
            alert(`Время вышло! Ваш финальный счет: ${score}`);
        }
    }, 1000);
}

function catchMouse() {
    score++;
    scoreDisplay.textContent = score;
    moveMouse();
}

mouse.addEventListener('click', catchMouse);
startBtn.addEventListener('click', () => {
    clearInterval(gameInterval);
    clearInterval(timerInterval);
    startGame();
});