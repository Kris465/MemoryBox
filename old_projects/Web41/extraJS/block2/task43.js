const prompt = require('prompt-sync')();

function checkDivisibility(a, b) {
  return ((a % b) * (b % a) === 0) ? 1 : 0;
}

const num1 = parseInt(prompt("Введите первое целое число: "));
const num2 = parseInt(prompt("Введите второе целое число: "));

if (isNaN(num1) || isNaN(num2)) {
    console.log("Ошибка: Введите целые числа.");
} else {
    const result = checkDivisibility(num1, num2);
    console.log(result);
}