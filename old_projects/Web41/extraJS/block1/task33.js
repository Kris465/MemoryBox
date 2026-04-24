const prompt = require('prompt-sync')();

const kol = prompt('Введите количество жителей: ');
const S = prompt('Введите площадь: ');
const plotnost = kol / S;

console.log(`Плотность насиления на метр/квадратный: ${plotnost}.`);
