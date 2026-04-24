const prompt = require('prompt-sync')();

function checkDigitsSum(number) {
    if (number < 10 || number > 99) {
        console.log("Пожалуйста, введите двузначное число.");
        return;
    }

    let firstDigit = Math.floor(number / 10); 
    let secondDigit = number % 10; 

    let sumOfDigits = firstDigit + secondDigit;

    if (sumOfDigits >= 10 && sumOfDigits <= 99) {
        console.log(`Сумма цифр (${sumOfDigits}) является двузначным числом.`);
    } else {
        console.log(`Сумма цифр (${sumOfDigits}) не является двузначным числом.`);
    }

    if (number > sumOfDigits) {
        console.log(`Число ${number} больше суммы его цифр (${sumOfDigits}).`);
    } else if (number < sumOfDigits) {
        console.log(`Число ${number} меньше суммы его цифр (${sumOfDigits}).`);
    } else {
        console.log(`Число ${number} равно сумме его цифр (${sumOfDigits}).`);
    }
}

let number = parseInt(prompt("Введите двузначное число:"));

if (!isNaN(number)) {
    checkDigitsSum(number);
} else {
    console.log("Пожалуйста, введите корректное число.");
}