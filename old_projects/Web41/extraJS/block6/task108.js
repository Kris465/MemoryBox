const prompt = require('prompt-sync')(); 

const n = parseInt(prompt("Введите сумму n:"), 10);
const denominations = [64, 32, 16, 8, 4, 2, 1];
const result = {};

let remaining = n;

for (let i = 0; i < denominations.length; i++) {
    const count = Math.floor(remaining / denominations[i]);
    result[denominations[i]] = count;
    remaining -= count * denominations[i];
}

console.log("Купюры для выплаты суммы " + n + ":");
for (const denom of denominations) {
    console.log(`Достоинство ${denom}: ${result[denom]} шт.`);
}