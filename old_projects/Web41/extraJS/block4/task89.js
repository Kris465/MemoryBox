const prompt = require('prompt-sync')();

const k = 2;


function calculateF(x) {
    const sinX = Math.sin(x);

    if (sinX > 0) {
        return k * x; 
    } else if (sinX === 0) {
        return k * x * x; 
    } else { 
        return x; 
    }
}


const inputX = parseFloat(prompt("Введите вещественное число x:"));


const resultF = calculateF(inputX);


console.log(`Значение функции f при x = ${inputX} равно: ${resultF}`);