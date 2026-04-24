const prompt = require('prompt-sync')();

function calculateY(x) {
    if (x < 0) {
        return x + 1; 
    } else if (x >= 0 && x < 1) {
        return -x + 1; 
    } else {
        return x - 1; 
    }
}

const inputX = parseFloat(prompt("Введите значение x:"));

if (!isNaN(inputX)) {
    const resultY = calculateY(inputX);
    console.log(`Значение функции y при x = ${inputX} равно: ${resultY}`);
} else {
    console.log("Пожалуйста, введите корректное вещественное число.");
}