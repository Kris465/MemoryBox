const prompt = require('prompt-sync')();
const userInput = prompt("Введите число: ");

if (userInput !== null) {
    console.log("Вы ввели число: " + userInput);
} else {
    console.log("Вы не ввели число.");
}
