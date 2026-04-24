const prompt = require('prompt-sync')();

function getAgePhrase(n) {
    let word;

    if (n === 1) {
        word = "год";
    } else if (n >= 2 && n <= 4) {
        word = "года";
    } else {
        word = "лет";
    }

    return `мне ${n} ${word}`;
}

const n = parseInt(prompt("Введите ваш возраст (от 1 до 99):"), 10);

if (n >= 1 && n <= 99) {
    console.log(getAgePhrase(n));
} else {
    console.log("Пожалуйста, введите число от 1 до 99.");
}