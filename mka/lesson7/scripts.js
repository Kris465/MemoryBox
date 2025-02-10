<<<<<<< HEAD
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
            piece.style.backgroundImage = 'url(images.jpg)';
            const x = (number % size) * 100;
            const y = Math.floor(number / size) * 100;
            piece.style.backgroundPosition = `-${x}px -${y}px`;
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
=======
function caesarCipher(text, shift) {
    const result = [];
    
    for (let char of text) {
        let code = char.charCodeAt(0);
        
        if (code >= 65 && code <= 90) {
            result.push(String.fromCharCode(((code - 65 + shift) % 26) + 65));
        } else if (code >= 97 && code <= 122) {
            result.push(String.fromCharCode(((code - 97 + shift) % 26) + 97));
        } 
        else if (code >= 1040 && code <= 1071) {
            result.push(String.fromCharCode(((code - 1040 + shift) % 32) + 1040));
        } else if (code >= 1072 && code <= 1103) {
            result.push(String.fromCharCode(((code - 1072 + shift) % 32) + 1072));
        } else {
            result.push(char);
        }
    }
    
    return result.join('');
}

document.getElementById('encryptBtn').addEventListener('click', function() {
    const inputText = document.getElementById('inputText').value;
    const shift = parseInt(document.getElementById('shift').value);
    const result = caesarCipher(inputText, shift);
    
    document.getElementById('result').textContent = result;
});

document.getElementById('decryptBtn').addEventListener('click', function() {
    const inputText = document.getElementById('inputText').value;
    const shift = parseInt(document.getElementById('shift').value);
    const result = caesarCipher(inputText, -shift);
    
    document.getElementById('result').textContent = result;
});
>>>>>>> 3bfa34956399c74ede40813d6d90bcd7ef3c7085
