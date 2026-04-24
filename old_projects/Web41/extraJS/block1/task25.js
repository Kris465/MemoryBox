const prompt = require('prompt-sync')();

let storona = prompt('Введите сторону квадрата: ');
let perimetr = storona*4;
console.log(`Периметр квадрата = ${perimetr}`);