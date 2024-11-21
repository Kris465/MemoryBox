const prompt = require('prompt-sync')();
const userInput = prompt("Введите число: ");

if (userInput !== null) {
    console.log(userInput + ', вот какое число Вы ввели');
} else {
    console.log("Вы не ввели число.");
}