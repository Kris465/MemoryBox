const prompt = require('prompt-sync')();

function areSameColor(a, b, c, d) {
    const color1 = (a + b) % 2; 
    const color2 = (c + d) % 2; 

    return color1 === color2;
}

const a = parseInt(prompt("Введите номер вертикали для первой клетки (1-8):"), 10);
const b = parseInt(prompt("Введите номер горизонтали для первой клетки (1-8):"), 10);
const c = parseInt(prompt("Введите номер вертикали для второй клетки (1-8):"), 10);
const d = parseInt(prompt("Введите номер горизонтали для второй клетки (1-8):"), 10);

if (areSameColor(a, b, c, d)) {
    console.log(`Клетки (${a}, ${b}) и (${c}, ${d}) одного цвета.`);
} else {
    console.log(`Клетки (${a}, ${b}) и (${c}, ${d}) разных цветов.`);
}