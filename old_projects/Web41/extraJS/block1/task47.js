const prompt = require('prompt-sync')();

function coordinat(x1,y1,x2,y2){
    const distance = Math.sqrt((x2 - x1)**2 + (y2- y1)**2);
    return distance
}
const x1 = prompt('Введите координаты x1:');
const y1 = prompt('Введите координаты y1:');
const x2 = prompt('Введите координаты x2:');
const y2 = prompt('Введите координаты y2:');

const result = coordinat(x1, y1, x2, y2);

console.log(`Расстояние между координатами: ${result}`);