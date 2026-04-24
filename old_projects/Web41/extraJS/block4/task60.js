const prompt = require('prompt-sync')();

function checkDigits(number) {

    if (number < 1000 || number > 9999) {
        console.log("Введите четырехзначное число.");
        return;
    }

    const numberStr = number.toString();

    const containsTwoOrSeven = numberStr.includes('2') || numberStr.includes('7');

    const containsThreeSixOrNine = numberStr.includes('3') || numberStr.includes('6') || numberStr.includes('9');


    console.log(`Цифры 2 или 7 ${containsTwoOrSeven ? "входят" : "не входят"} в число ${number}.`);
    console.log(`Цифры 3, 6 или 9 ${containsThreeSixOrNine ? "входят" : "не входят"} в число ${number}.`);
}

const number = parseInt(prompt("Введите четырехзначное число:"));


if (isNaN(number)) {
    console.log("Пожалуйста, введите корректное число.");
} else {
    checkDigits(number);
}