const prompt = require('prompt-sync')();

const n = parseInt(prompt("Введите количество человек:"), 10);
const heights = [];

for (let i = 0; i < n; i++) {
    heights.push(parseFloat(prompt(`Введите рост человека ${i + 1}:`)));
}

const maxHeight = Math.max(...heights);
const minHeight = Math.min(...heights);
const difference = maxHeight - minHeight;

console.log(`Разница между самым высоким и самым низким ростом: ${difference}`);