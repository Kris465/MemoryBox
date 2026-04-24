const prompt = require('prompt-sync')();

function calculateZ(a) {
    if (a < 0) {
        return 1;
    } else if (a >= 0 && a < 1) {
        return a; 
    } else { 
        return 0; 
    }
}

const inputA = parseFloat(prompt("Введите значение a:"));

const resultZ = calculateZ(inputA);

console.log(`Значение функции z при a = ${inputA} равно: ${resultZ}`);