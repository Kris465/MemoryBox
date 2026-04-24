const prompt = require('prompt-sync')();

let n;
do {
    const inputN = prompt("Введите количество человек (целое число):");
    if (inputN === null) continue;
    if (/^\d+$/.test(inputN.trim())) {
        n = parseInt(inputN.trim(), 10);
        if (n > 0) break;
    }
} while (true);

const heights = [];

for (let i = 0; i < n; i++) {
    let input;
    do {
        input = prompt(`Введите рост человека ${i + 1} (число):`);
        if (input === null) continue;
        input = input.trim();
    } while (input === '' || isNaN(parseFloat(input)));
    heights.push(parseFloat(input));
}

const maxHeight = Math.max(...heights);
const minHeight = Math.min(...heights);
const difference = maxHeight - minHeight;

console.log(`Разница между самым высоким и самым низким ростом: ${difference}`);