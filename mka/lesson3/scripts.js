let randomNumber = Math.floor(Math.random() * 100) + 1;
let attempts = 0;

const guessButton = document.getElementById('guessButton');
const guessInput = document.getElementById('guessInput');
const resultText = document.getElementById('resultText');
const restartButton = document.getElementById('restartButton');

guessButton.addEventListener('click', () => {
    const userGuess = Number(guessInput.value);
    attempts++;

    if (userGuess < 1 || userGuess > 100) {
        resultText.textContent = 'Введите число от 1 до 100.';
        return;
    }

    if (userGuess === randomNumber) {
        resultText.textContent = `Поздравляю! Вы угадали число ${randomNumber} за ${attempts} попыток.`;
        guessButton.disabled = true;
        restartButton.style.display = 'inline';
    } else if (userGuess < randomNumber) {
        resultText.textContent = 'Слишком мало! Попробуйте снова.';
    } else {
        resultText.textContent = 'Слишком много! Попробуйте снова.';
    }
});

restartButton.addEventListener('click', () => {
    randomNumber = Math.floor(Math.random() * 100) + 1;
    attempts = 0;
    guessInput.value = '';
    resultText.textContent = '';
    guessButton.disabled = false;
    restartButton.style.display = 'none';
});
