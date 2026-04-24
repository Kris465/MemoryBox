const prompt = require('prompt-sync')();

function compareDigits(number) {
    if (number < 100 || number > 999) {
        console.log("Пожалуйста, введите трехзначное число.");
        return;
    }

    let firstDigit = Math.floor(number / 100);
    let secondDigit = Math.floor((number % 100) / 10);
    let lastDigit = number % 10; 

    if (firstDigit > lastDigit) {
        console.log(`Первая цифра (${firstDigit}) больше последней (${lastDigit}).`);
    } else if (firstDigit < lastDigit) {
        console.log(`Первая цифра (${firstDigit}) меньше последней (${lastDigit}).`);
    } else {
        console.log(`Первая цифра (${firstDigit}) равна последней (${lastDigit}).`);
    }

    if (firstDigit > secondDigit) {
        console.log(`Первая цифра (${firstDigit}) больше второй (${secondDigit}).`);
    } else if (firstDigit < secondDigit) {
        console.log(`Первая цифра (${firstDigit}) меньше второй (${secondDigit}).`);
    } else {
        console.log(`Первая цифра (${firstDigit}) равна второй (${secondDigit}).`);
    }

    if (secondDigit > lastDigit) {
        console.log(`Вторая цифра (${secondDigit}) больше последней (${lastDigit}).`);
    } else if (secondDigit < lastDigit) {
        console.log(`Вторая цифра (${secondDigit}) меньше последней (${lastDigit}).`);
    } else {
        console.log(`Вторая цифра (${secondDigit}) равна последней (${lastDigit}).`);
    }
}

let number = parseInt(prompt("Введите трехзначное число:"));

if (!isNaN(number)) {
    compareDigits(number);
} else {
    console.log("Пожалуйста, введите корректное число.");
}