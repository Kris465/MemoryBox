const prompt = require('prompt-sync')(); 

const numStr = prompt("Введите натуральное число:");
const num = parseInt(numStr, 10);

function isFibonacci(n) {
    let a = 1;
    let b = 1;
    if (n === 1) return true;
    while (b < n) {
        const next = a + b;
        a = b;
        b = next;
        if (b === n) return true;
    }
    return false;
}

const result = isFibonacci(num);
console.log(`Число ${num} ${result ? "является" : "не является"} членом последовательности Фибоначчи.`);