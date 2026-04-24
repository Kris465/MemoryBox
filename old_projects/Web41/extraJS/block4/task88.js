const prompt = require('prompt-sync')();

function calculateF(y) {
    if (y < 0) {
        return 2; 
    } else if (y === 0) {
        return 0; 
    } else if (y === 2) {
        return y * y; 
    } else { 
        return 3; 
    }
}


const inputY = parseFloat(prompt("Введите вещественное число y:"));


const resultF = calculateF(inputY);


console.log(`Значение функции f при y = ${inputY} равно: ${resultF}`);