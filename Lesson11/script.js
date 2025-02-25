const cards = [
    'A', 'A', 'B', 'B', 'C', 'C', 'D', 'D',
    'E', 'E', 'F', 'F', 'G', 'G', 'H', 'H'
];

let firstCard = null;
let secondCard = null;
let lockBoard = false;

const gameContainer = document.getElementById('game-container');
const restartButton = document.getElementById('restart-button');

function shuffle(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
}

function createCard(cardValue) {
    const card = document.createElement('div');
    card.classList.add('card');
    card.dataset.value = cardValue;

    // Создаем элемент для текста
    const cardText = document.createElement('span');
    cardText.textContent = cardValue;
    cardText.classList.add('card-text');
    
    // Добавляем текст на карточку
    card.appendChild(cardText);

    card.addEventListener('click', flipCard);
    
    gameContainer.appendChild(card);
}


function flipCard() {
    if (lockBoard || this === firstCard) return;

    this.classList.add('flipped');
    
    if (!firstCard) {
        firstCard = this;
        return;
    }

    secondCard = this;

    checkForMatch();
}

function checkForMatch() {
    lockBoard = true;

    const isMatch = firstCard.dataset.value === secondCard.dataset.value;

    isMatch ? disableCards() : unflipCards();
}

function disableCards() {
    firstCard.classList.add('matched');
    secondCard.classList.add('matched');

    resetBoard();
}

function unflipCards() {
    setTimeout(() => {
        firstCard.classList.remove('flipped');
        secondCard.classList.remove('flipped');

        resetBoard();
    }, 1000);
}

function resetBoard() {
    [firstCard, secondCard, lockBoard] = [null, null, false];
}

function startGame() {
    shuffle(cards);
    
    gameContainer.innerHTML = '';
    
    cards.forEach(createCard);
}

restartButton.addEventListener('click', startGame);

startGame();
