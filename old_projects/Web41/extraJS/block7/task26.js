const prompt = require('prompt-sync')();

const n = parseInt(prompt("Введите количество дней в месяце:"), 10);
let countBelowZero = 0;
for (let i = 0; i < n; i++) {
    const temp = parseFloat(prompt(`Введите температуру в день ${i + 1}:`));
    if (temp < 0) {
        countBelowZero++;
    }
}
console.log("Количество дней с температурой ниже 0°C:", countBelowZero);