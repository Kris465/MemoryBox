const prompt = require('prompt-sync')();

function getIntegerInput(promptMessage) {
    let input;
    do {
        input = prompt(promptMessage);
    } while (isNaN(input) || input === null || input.trim() === "" || !Number.isInteger(Number(input)));
    return parseInt(input, 10);
}

let N = getIntegerInput("Введите целое число N:");

let conditionA = (N % 5 === 0) || (N % 7 === 0);

let conditionB = (N % 4 === 0) && (N % 10 !== 0);

console.log(`Условие A (N кратно пяти или семи): ${conditionA}`); 
console.log(`Условие B (N кратно четырем и не оканчивается нулем): ${conditionB}`); 