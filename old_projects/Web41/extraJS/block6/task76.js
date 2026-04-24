const prompt = require('prompt-sync')(); 

const numStr = prompt("Введите число:");
const num = parseInt(numStr, 10);

function isPowerOf(base, number) {
    if (number < 1) return false;
    while (number > 1) {
        if (number % base !== 0) return false;
        number = number / base;
    }
    return true;
}

const isPowerOf3 = isPowerOf(3, num);
const isPowerOf5 = isPowerOf(5, num);

console.log(`Число ${num} является степенью 3: ${isPowerOf3}`);
console.log(`Число ${num} является степенью 5: ${isPowerOf5}`);