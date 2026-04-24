const prompt = require('prompt-sync')();
let num = prompt("Введите число: ");
num = Number(num);
if (num % 2 === 0) {
    console.log(num + " является четным числом.");
} else {
    console.log(num + " является нечетным числом.");
}