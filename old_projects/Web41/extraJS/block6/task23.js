const prompt = require('prompt-sync')();

const numberStr = prompt("Введите натуральное число:");
const a = parseInt(prompt("Введите цифру a (от 0 до 8):"));
const z = parseInt(prompt("Введите число z (2, 3 или 4):"));
const x = prompt("Введите цифру x:");
const y = prompt("Введите цифру y:");

let countA = 0;
let countZ = 0;
let sumGreaterA = 0;
let countX = 0;
let countY = 0;

for (let digit of numberStr) {
    if (digit === a.toString()) {
        countA++;
    }
    if (parseInt(digit) === z) {
        countZ++;
    }
    if (parseInt(digit) > a) {
        sumGreaterA += parseInt(digit);
    }
    if (digit === x) {
        countX++;
    }
    if (digit === y) {
        countY++;
    }
}

console.log("а) Количество встречающихся цифр а: " + countA);
console.log("б) Количество цифр, кратных z: " + countZ);
console.log("в) Сумма цифр, больших а: " + sumGreaterA);
console.log("г) Количество встречаний цифры x: " + countX);
console.log("д) Количество встречаний цифры y: " + countY);