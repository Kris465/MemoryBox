const prompt = require('prompt-sync')();

const ob = prompt('Введите объем тела: ');
const massa = prompt('Введите массу тела: ');
const plotnost = massa / ob;

console.log(`Плотность тела: ${plotnost}.`);
