const prompt = require('prompt-sync')();
let radius = prompt("Введите радиус окружности: ");
let result = Math.PI * Math.pow(radius, 2);
console.log(`площадь окружности: ${result}`)