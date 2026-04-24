const prompt = require('prompt-sync')();

const userInput = prompt("Введите натуральное число:");
const n = parseInt(prompt("Введите количество последних цифр для суммирования:"));

if (!isNaN(userInput) && !isNaN(n) && n > 0 && n <= userInput.length) {
    let sum = 0;
    let length = userInput.length;

    for (let i = length - n; i < length; i++) {
        sum += Number(userInput[i]);
    }

    console.log(`Сумма последних ${n} цифр числа ${userInput} равна: ${sum}`);
} else {
    console.log("Пожалуйста, введите корректные значения.");
}