const prompt = require('prompt-sync')();

function checkNumber(n) {
    if (n % 2 === 0) {
        console.log(`${n} является четным числом.`);
    } else {
        console.log(`${n} является нечетным числом.`);
    }

    if (n % 10 === 7) {
        console.log(`${n} оканчивается на 7.`);
    } else {
        console.log(`${n} не оканчивается на 7.`);
    }
}

let number = parseInt(prompt("Введите натуральное число:"));
if (!isNaN(number) && number > 0) {
    checkNumber(number);
} else {
    console.log("Пожалуйста, введите корректное натуральное число.");
}