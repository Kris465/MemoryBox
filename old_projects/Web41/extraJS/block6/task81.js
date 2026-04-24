const prompt = require('prompt-sync')(); 

const numStr = prompt("Введите натуральное число:");
const a = prompt("Введите цифру a:");
const b = prompt("Введите цифру b:");

let countA = 0;
let countB = 0;

for (let digit of numStr) {
    if (digit === a) countA++;
    if (digit === b) countB++;
}

if (countA < countB) {
    console.log(`Цифра ${a} встречается реже, чем цифра ${b}.`);
} else {
    console.log(`Цифра ${a} не встречается реже, чем цифра ${b}.`);
}