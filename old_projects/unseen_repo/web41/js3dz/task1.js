const prompt = require('prompt-sync')();

let start = parseInt(prompt('Введите начало диапазона: '));
let end = parseInt(prompt('Введите конец диапазона: '));
let sum = 0;

for (let i = start; i <= end; i++) {
    sum += i;
}

console.log(`Сумма всех чисел в диапазоне от ${start} до ${end}: ${sum}`);
