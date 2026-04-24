const prompt = require('prompt-sync')();

function calculateY(x) {
    if (x < -1) {
        return 1;
    } else if (x >= -1 && x < 1) {
        return x * x; 
    } else { 
        return 1;
    }
}

const inputX = parseFloat(prompt("Введите значение x:"));
const resultY = calculateY(inputX);
console.log(`Значение функции y при x = ${inputX} равно: ${resultY}`);