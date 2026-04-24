const prompt = require('prompt-sync')();

function checkDigits(number, n) {
    if (number < 100 || number > 999) {
        console.log("Введите трехзначное число.");
        return;
    }
    const hundreds = Math.floor(number / 100); 
    const tens = Math.floor((number % 100) / 10); 
    const units = number % 10; 

    const containsSix = (hundreds === 6 || tens === 6 || units === 6);
    const containsN = (hundreds === n || tens === n || units === n);

    console.log(`Цифра 6 ${containsSix ? "входит" : "не входит"} в число ${number}.`);
    console.log(`Цифра ${n} ${containsN ? "входит" : "не входит"} в число ${number}.`);
}

const number = parseInt(prompt("Введите трехзначное число:"));

const n = parseInt(prompt("Введите цифру n (0-9):"));

if (n < 0 || n > 9 || isNaN(n)) {
    console.log("Цифра n должна быть от 0 до 9.");
} else {
    checkDigits(number, n);
}