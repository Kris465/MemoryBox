const prompt = require('prompt-sync')();

function getIntegerInput(promptMessage) {
    let input;
    do {
        input = prompt(promptMessage);
    } while (isNaN(input) || input === null || input.trim() === "" || !Number.isInteger(Number(input)));
    return parseInt(input, 10);
}

let A = getIntegerInput("Введите целое число A:");

let conditionA = (A % 2 === 0) || (A % 3 === 0);

let conditionB = (A % 3 !== 0) && (A % 10 === 0);

console.log(`Условие A (A кратно двум или трем): ${conditionA}`); 
console.log(`Условие B (A не кратно трем и оканчивается нулем): ${conditionB}`); 