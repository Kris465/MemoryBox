const prompt = require('prompt-sync')();

let R = prompt("введите внешний радиус кольца: ");
let r = prompt("введите внутренний радиус кольца: ");

let S = Math.PI * (Math.pow(R, 2) - Math.pow(r, 2));
console.log(`Площадь кольца равна: ${S}`);