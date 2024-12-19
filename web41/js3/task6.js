const prompt = require('prompt-sync')();

let initialVolume = parseFloat(prompt('Введите первоначальный объем воды (в литрах): '));
let days = 0;

while (initialVolume >= 10) {
    initialVolume *= 0.9; // Уменьшаем объем на 10%
    days++;
}

console.log(`Количество дней, на которые хватит воды: ${days}`);
