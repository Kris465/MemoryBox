const prompt = require('prompt-sync')();

let positiveCount = 0;
let negativeCount = 0;
let zeroCount = 0;
let evenCount = 0;
let oddCount = 0;

for (let i = 0; i < 10; i++) {
    let number = parseInt(prompt('Введите число: '));

    if (number > 0) positiveCount++;
    else if (number < 0) negativeCount++;
    else zeroCount++;

    if (number % 2 === 0) evenCount++;
    else oddCount++;
}

console.log(`Положительные: ${positiveCount}, Отрицательные: ${negativeCount}, Нули: ${zeroCount}`);
console.log(`Четные: ${evenCount}, Нечетные: ${oddCount}`);
