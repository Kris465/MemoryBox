const prompt = require('prompt-sync')();

function calculateF(x) {
    const sinX = Math.sin(x);
    let k;

    if (sinX >= 0) {
        k = x * x; 
    } else {
        k = Math.abs(x);
    }

    if (Math.abs(x) < k) {
        return Math.abs(x); 
    } else {
        return k * x;
    }
}

const inputX = parseFloat(prompt("Введите вещественное число x:"));

if (!isNaN(inputX)) {
    const resultF = calculateF(inputX); 
    console.log(`Значение функции f при x = ${inputX} равно: ${resultF}`);
} else {
    console.log("Пожалуйста, введите корректное вещественное число.");
}