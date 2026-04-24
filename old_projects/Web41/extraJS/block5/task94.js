const prompt = require('prompt-sync')();

const userInput = prompt("Введите шестизначное число:");

if (userInput.length === 6 && !isNaN(userInput)) {
    let sum = 0;

    for (let i = 0; i < userInput.length; i++) {
        sum += Number(userInput[i]);
    }

    console.log(`Сумма цифр числа ${userInput} равна ${sum}`);
} else {
    console.log("Пожалуйста, введите корректное шестизначное число.");
}