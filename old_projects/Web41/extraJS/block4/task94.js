const prompt = require('prompt-sync')();

function determineResult(points) {
    if (points === 3) {
        return "Выигрыш"; 
    } else if (points === 1) {
        return "Ничья"; 
    } else if (points === 0) {
        return "Проигрыш"; 
    } else {
        return "Некорректное количество очков"; 
    }
}

const inputPoints = parseInt(prompt("Введите количество очков, полученных командой:"));

if (!isNaN(inputPoints)) {
    const result = determineResult(inputPoints);
    console.log(`Результат игры: ${result}`); 
} else {
    console.log("Пожалуйста, введите корректное целое число для количества очков.");
}