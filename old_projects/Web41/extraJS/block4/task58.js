const prompt = require('prompt-sync')();

function checkDigits(number) {
    if (number < 100 || number > 999) {
        console.log("Введите трехзначное число.");
        return;
    }

    const hundreds = Math.floor(number / 100); 
    const tens = Math.floor((number % 100) / 10); 
    const units = number % 10;
    const containsFourOrSeven = (hundreds === 4 || tens === 4 || units === 4 || 
                                 hundreds === 7 || tens === 7 || units === 7);

    const containsThreeSixOrNine = (hundreds === 3 || tens === 3 || units === 3 || 
                                     hundreds === 6 || tens === 6 || units === 6 || 
                                     hundreds === 9 || tens === 9 || units === 9);

    console.log(`Цифры 4 или 7 ${containsFourOrSeven ? "входят" : "не входят"} в число ${number}.`);
    console.log(`Цифры 3, 6 или 9 ${containsThreeSixOrNine ? "входят" : "не входят"} в число ${number}.`);
}

const number = parseInt(prompt("Введите трехзначное число:"));

if (isNaN(number)) {
    console.log("Пожалуйста, введите корректное число.");
} else {
    checkDigits(number);
}