const prompt = require('prompt-sync')();

let rate = parseFloat(prompt('Введите годовую депозитную ставку (в процентах): '));
let years = 0;
let amount = 1; // Начальная сумма

while (amount < 2) {
    amount *= (1 + rate / 100);
    years++;
}

console.log(`Количество лет, чтобы вклад удвоился: ${years}`);
