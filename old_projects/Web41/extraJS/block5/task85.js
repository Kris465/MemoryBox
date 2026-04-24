const prompt = require('prompt-sync')();

const userInput = prompt("Введите пятизначное число:");

if (userInput.length === 5 && !isNaN(userInput)) {
    const reversedNumber = userInput.split('').reverse().join('');
    console.log(`Число, получаемое при прочтении цифр справа налево: ${reversedNumber}`);
} else {
    console.log("Пожалуйста, введите корректное пятизначное число.");
}