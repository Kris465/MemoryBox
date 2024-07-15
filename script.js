document.addEventListener('DOMContentLoaded', () => {
    const X_CLASS = 'x';
    const O_CLASS = 'o';
    let currentPlayer = X_CLASS;
    const cellElements = document.querySelectorAll('.cell');

    cellElements.forEach(cell => {
        cell.addEventListener('click', handleClick, { once: true });
    });

    function handleClick(e) {
        const cell = e.target;
        if (cell.classList.contains(X_CLASS) || cell.classList.contains(O_CLASS)) {
            return; // Чтобы игровое поле не перезаполнялось, если ячейка уже занята
        }
        const currentClass = currentPlayer === X_CLASS ? X_CLASS : O_CLASS;
        placeMark(cell, currentClass);
        if (checkWin(currentClass)) {
            alert(`${currentClass === X_CLASS ? 'X' : 'O'} wins!`);
        } else if (isDraw()) {
            alert(`It's a draw!`);
        } else {
            currentPlayer = currentPlayer === X_CLASS ? O_CLASS : X_CLASS;
        }
    }
    
    function placeMark(cell, currentClass) {
        cell.classList.add(currentClass);
    }
    

    function placeMark(cell, currentClass) {
        cell.classList.add(currentClass);
    }

    const WINNING_COMBINATIONS = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], // Горизонтальные линии
        [0, 3, 6], [1, 4, 7], [2, 5, 8], // Вертикальные линии
        [0, 4, 8], [2, 4, 6] // Диагонали
    ];

    function checkWin(currentClass) {
        return WINNING_COMBINATIONS.some(combination => {
            return combination.every(index => {
                return cellElements[index].classList.contains(currentClass);
            });
        });
    }

    function isDraw() {
        return [...cellElements].every(cell => {
            return cell.classList.contains(X_CLASS) || cell.classList.contains(O_CLASS);
        });
    }
});
