let firstCard = null;
let secondCard = null;
let lockBoard = false;

function flipCard(card) {
    if (lockBoard) return;
    
    const cardInner = card.querySelector('.card-inner');
    cardInner.style.transform = 'rotateY(180deg)';
    
    if (!firstCard) {
        firstCard = card;
        return;
    }

    secondCard = card;

    checkForMatch();
}

function checkForMatch() {
    const isMatch = firstCard.dataset.character === secondCard.dataset.character;

    isMatch ? disableCards() : unflipCards();
}

function disableCards() {
    firstCard.removeEventListener('click', flipCard);
    secondCard.removeEventListener('click', flipCard);
    
    resetBoard();
}

function unflipCards() {
    lockBoard = true;

    setTimeout(() => {
        const firstCardInner = firstCard.querySelector('.card-inner');
        const secondCardInner = secondCard.querySelector('.card-inner');
        
        firstCardInner.style.transform = 'rotateY(0deg)';
        secondCardInner.style.transform = 'rotateY(0deg)';
        
        resetBoard();
    }, 1500);
}

function resetBoard() {
    [firstCard, secondCard, lockBoard] = [null, null, false];
}
