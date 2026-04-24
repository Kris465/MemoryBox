const prompt = require('prompt-sync')();
const target = parseInt(prompt("Введите целевое число (например, 237): "));

for (let x = 100; x <= 999; x++) {
    if (Math.floor(x / 10) * 10 + (x % 10) === target) {
        console.log(`Найдено число x: ${x}`);
        break;
    }
}