const prompt = require('prompt-sync')(); 

const pointsInput = prompt("Введите количество очков 20 команд через пробел (по убыванию):");
const points = pointsInput.split(' ').map(Number);

const N = Number(prompt("Введите количество очков искомой команды:"));


const position = points.indexOf(N) + 1;


console.log(`Команда с ${N} очками заняла ${position}-е место`);