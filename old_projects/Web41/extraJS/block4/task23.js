const prompt = require('prompt-sync')();

function checkDigits(number) {
    if (number < 10 || number > 99) {
        console.log("Пожалуйста, введите двузначное число.");
        return;
    }

    let firstDigit = Math.floor(number / 10); 
    let secondDigit = number % 10; 

    if (firstDigit > secondDigit) {
        console.log(`Первая цифра (${firstDigit}) больше второй цифры (${secondDigit}).`);
    } else if (firstDigit < secondDigit) {
        console.log(`Вторая цифра (${secondDigit}) больше первой цифры (${firstDigit}).`);
    } else {
        console.log(`Цифры одинаковы: ${firstDigit} и ${secondDigit}.`);
    }
}

let number = parseInt(prompt("Введите двузначное число:"));

if (!isNaN(number)) {
    checkDigits(number);
} else {
    console.log("Пожалуйста, введите корректное число.");
}