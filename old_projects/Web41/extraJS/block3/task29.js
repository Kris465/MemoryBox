const prompt = require('prompt-sync')();


function getNumberInput(promptMessage) {
    let input;
    do {
        input = prompt(promptMessage);
    } while (isNaN(input) || input === null || input.trim() === "");
    return Number(input);
}


let X = getNumberInput("Введите значение для X:");
let Y = getNumberInput("Введите значение для Y:");
let Z = getNumberInput("Введите значение для Z:");


let conditionA = (X % 2 !== 0) && (Y % 2 !== 0);


let conditionB = (X < 20) !== (Y < 20);

    
let conditionC = (X === 0) || (Y === 0);


let conditionD = (X < 0) && (Y < 0) && (Z < 0);


let conditionE = (X % 5 === 0) + (Y % 5 === 0) + (Z % 5 === 0) === 1;


let conditionF = (X > 100) || (Y > 100) || (Z > 100);

``
console.log(`Условие A: ${conditionA}`); 
console.log(`Условие B: ${conditionB}`); 
console.log(`Условие C: ${conditionC}`); 
console.log(`Условие D: ${conditionD}`); 
console.log(`Условие E: ${conditionE}`); 
console.log(`Условие F: ${conditionF}`); 