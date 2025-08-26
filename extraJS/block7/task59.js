const prompt = require('prompt-sync')();

const n = parseInt(prompt("Введите количество квадратов:"), 10);
const areas = [];

for (let i = 0; i < n; i++) {
    const area = parseFloat(prompt(`Введите площадь квадрата ${i + 1}:`));
    areas.push(area);
}

let maxArea = areas[0];

for (let i = 1; i < n; i++) {
    if (areas[i] > maxArea) {
        maxArea = areas[i];
    }
}

const side = Math.sqrt(maxArea);
const diagonal = side * Math.sqrt(2);

console.log(`Длина диагонали самого большого квадрата: ${diagonal}`);