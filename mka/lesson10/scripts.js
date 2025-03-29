const gameArea = document.getElementById('gameArea');
const player = document.getElementById('player');
const scoreDisplay = document.getElementById('score');
let score = 0;

let playerPosition = 175;
document.addEventListener('keydown', movePlayer);

function movePlayer(event) {
    if (event.key === 'ArrowLeft' && playerPosition > 0) {
        playerPosition -= 15;
    } else if (event.key === 'ArrowRight' && playerPosition < 350) {
        playerPosition += 15;
    }
    player.style.left = playerPosition + 'px';
}

function createObstacle() {
    const obstacle = document.createElement('div');
    obstacle.classList.add('obstacle');
    obstacle.style.left = Math.random() * (gameArea.clientWidth - 30) + 'px';
    gameArea.appendChild(obstacle);
    
    let obstacleInterval = setInterval(() => {
        const obstacleTop = parseInt(window.getComputedStyle(obstacle).getPropertyValue('top'));
        
        if (obstacleTop > gameArea.clientHeight) {
            clearInterval(obstacleInterval);
            gameArea.removeChild(obstacle);
            score++;
            scoreDisplay.innerText = 'Очки: ' + score;
        } else if (obstacleTop + 30 >= gameArea.clientHeight - 60 && 
                   parseInt(obstacle.style.left) >= playerPosition - 30 && 
                   parseInt(obstacle.style.left) <= playerPosition + 50) {
            clearInterval(obstacleInterval);
            alert('Игра окончена! Ваши очки: ' + score);
            location.reload();
        }
        
        obstacle.style.top = obstacleTop + 5 + 'px';
    }, 100);
}

setInterval(createObstacle, 1000);
