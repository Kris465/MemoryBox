const prompt = require('prompt-sync')();

function checkDigits(number) {
    if (number < 10 || number > 99) {
        console.log("Введите двузначное число.");
        return;
    }

    const tens = Math.floor(number / 10); 
    const units = number % 10; 

    const containsFourOrSeven = (tens === 4 || units === 4 || tens === 7 || units === 7);
    const containsThreeSixOrNine = (tens === 3 || units === 3 || tens === 6 || units === 6 || tens === 9 || units === 9);

    console.log(`Цифры 4 или 7 ${containsFourOrSeven ? "входят" : "не входят"} в число ${number}.`);
    console.log(`Цифры 3, 6 или 9 ${containsThreeSixOrNine ? "входят" : "не входят"} в число ${number}.`);
}

const number = parseInt(prompt("Введите двузначное число:"));

if (isNaN(number)) {
    console.log("Пожалуйста, введите корректное число.");
} else {
    checkDigits(number);
}