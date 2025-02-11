const puzzleContainer = document.getElementById('puzzle-container');
const shuffleButton = document.getElementById('shuffle-button');

let puzzle = [];
const size = 3;

function initPuzzle() {
    puzzle = [];
    for (let i = 0; i < size * size; i++) {
        puzzle.push(i);
    }
    renderPuzzle();
}

function renderPuzzle() {
    puzzleContainer.innerHTML = '';
    puzzle.forEach((number, index) => {
        const piece = document.createElement('div');
        piece.classList.add('puzzle-piece');
        if (number !== 0) {
            piece.style.backgroundImage = 'url(image.jpg)';
            const x = (number % size) * 100;
            const y = Math.floor(number / size) * 100;
            piece.style.backgroundPosition = -${x}px -${y}px;
            piece.addEventListener('click', () => movePiece(index));
        } else {
            piece.classList.add('empty');
        }
        puzzleContainer.appendChild(piece);
    });
}


function movePiece(index) {
    const emptyIndex = puzzle.indexOf(0);
    
    const isAdjacent = (index === emptyIndex - 1 && index % size !== size - 1) ||
                      (index === emptyIndex + 1 && emptyIndex % size !== size - 1) ||
                      (index === emptyIndex - size) ||
                      (index === emptyIndex + size);

    if (isAdjacent) {
        [puzzle[index], puzzle[emptyIndex]] = [puzzle[emptyIndex], puzzle[index]];
        renderPuzzle();
    }
}

function shufflePuzzle() {
    for (let i = puzzle.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [puzzle[i], puzzle[j]] = [puzzle[j], puzzle[i]];
    }
    renderPuzzle();
}

shuffleButton.addEventListener('click', shufflePuzzle);
initPuzzle();
