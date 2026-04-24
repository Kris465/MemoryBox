const prompt = require('prompt-sync')();

function checkDigits(number, b) {

    if (number < 1000 || number > 9999) {
        console.log("Введите четырехзначное число.");
        return;
    }

    const numberStr = number.toString();

    const containsFour = numberStr.includes('4');

    const containsB = numberStr.includes(b.toString());

    console.log(`Цифра 4 ${containsFour ? "входит" : "не входит"} в число ${number}.`);
    console.log(`Цифра ${b} ${containsB ? "входит" : "не входит"} в число ${number}.`);
}

const number = parseInt(prompt("Введите четырехзначное число:"));

const b = prompt("Введите цифру b (0-9):");

if (b.length !== 1 || isNaN(b) || b < 0 || b > 9) {
    console.log("Цифра b должна быть от 0 до 9.");
} else {
    checkDigits(number, b);
}