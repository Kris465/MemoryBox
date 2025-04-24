const player = document.getElementById("player");
const game = document.getElementById("game");
const scoreElement = document.getElementById("score");

let playerX = 180;
let playerY = 300;
let playerSpeedX = 0;
let playerSpeedY = 0;
let platforms = [];
let score = 0;
let isGameOver = false;

function createPlatforms() {
    for (let i = 0; i < 8; i++) {
        platforms.push({
            x: Math.random() * 320,
            y: 600 - i * 100,
        });
    }
}

function drawPlatforms() {
    document.querySelectorAll(".platform").forEach(el => el.remove());
    platforms.forEach(platform => {
        const platformElement = document.createElement("div");
        platformElement.className = "platform";
        platformElement.style.left = `${platform.x}px`;
        platformElement.style.top = `${platform.y}px`;
        game.appendChild(platformElement);
    });
}

function updatePlayer() {
    playerSpeedY += 0.2;
    playerY += playerSpeedY;
    playerX += playerSpeedX;

    if (playerX < 0) playerX = 360;
    if (playerX > 360) playerX = 0;

    platforms.forEach(platform => {
        if (
            playerY + 60 >= platform.y &&
            playerY + 60 <= platform.y + 20 &&
            playerX + 40 >= platform.x &&
            playerX <= platform.x + 80 &&
            playerSpeedY > 0
        ) {
            playerSpeedY = -10;
        }
    });

    if (playerY > 600) {
        alert(`Игра окончена! Счёт: ${score}`);
        resetGame();
    }

    if (playerY < 300) {
        const delta = 300 - playerY;
        playerY = 300;
        platforms.forEach(platform => {
            platform.y += delta;
            if (platform.y > 600) {
                platform.y = 0;
                platform.x = Math.random() * 320;
                score += 10;
                scoreElement.textContent = score;
            }
        });
    }

    player.style.left = `${playerX}px`;
    player.style.top = `${playerY}px`;
}

document.addEventListener("keydown", (e) => {
    if (e.key === "ArrowLeft") playerSpeedX = -5;
    if (e.key === "ArrowRight") playerSpeedX = 5;
});

document.addEventListener("keyup", (e) => {
    if (e.key === "ArrowLeft" || e.key === "ArrowRight") playerSpeedX = 0;
});

function resetGame() {
    playerY = 300;
    playerX = 180;
    playerSpeedY = 0;
    platforms = [];
    score = 0;
    scoreElement.textContent = "0";
    createPlatforms();
}

createPlatforms();
drawPlatforms();

function gameLoop() {
    if (!isGameOver) {
        updatePlayer();
        drawPlatforms();
        requestAnimationFrame(gameLoop);
    }
}

gameLoop();