const prompt = require('prompt-sync')();

const c1 = 2;
const c2 = 7;
const c3 = 4;
const c4 = 9;
const c5 = 12;
const c6 = 15;
const c7 = 8;
const c8 = 3;
const c9 = 6;
const c10 = 11;
const c11 = 14;
const c12 = 20;

const numbers = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12];

const evenNumbers = numbers.filter(num => num % 2 === 0);

const sumEven = evenNumbers.reduce((sum, num) => sum + num, 0);

const averageEven = sumEven / evenNumbers.length;

console.log("Среднее арифметическое четных чисел:", averageEven);