const prompt = require('prompt-sync')();


function calculateF(x) {
    if (x < 0) {
        return x; 
    } else if (x >= 0 && x < 1) {
        return 0; 
    } else if (x === 1) {
        return 2; 
    } else { 
        return x * x; 
    }
}


const inputX = parseFloat(prompt("Введите вещественное число x:"));


const resultF = calculateF(inputX);


console.log(`Значение функции f при x = ${inputX} равно: ${resultF}`);