const prompt = require('prompt-sync')(); 

const sequence = [];
for (let i = 0; i < 20; i++) {
    const numStr = prompt(`Введите число ${i + 1} (от 0 до 66):`);
    const num = parseInt(numStr, 10);
    if (isNaN(num) || num < 0 || num > 66) {
        alert("Некорректное число. Попробуйте снова.");
        i--;
        continue;
    }
    sequence.push(num);
}

let conditionA = true;
for (let num of sequence) {
    const lastDigit = num % 10;
}

let conditionB = true;
for (let num of sequence) {
    const leftDigit = Math.floor(num / 10);
    const rightDigit = num % 10;
    if (!(leftDigit >=0 && leftDigit <=6 && rightDigit >=0 && rightDigit <=6)) {
        conditionB = false;
        break;
    }
}

console.log("Условие (а):", conditionA ? "выполнено" : "не выполнено");
console.log("Условие (б):", conditionB ? "выполнено" : "не выполнено");