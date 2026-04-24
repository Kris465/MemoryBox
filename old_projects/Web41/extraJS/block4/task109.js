const prompt = require('prompt-sync')();

function getCardRank(k) {
    switch (k) {
        case 6:
            return "Шестёрка";
        case 7:
            return "Семёрка";
        case 8:
            return "Восьмёрка";
        case 9:
            return "Девятка";
        case 10:
            return "Десятка";
        case 11:
            return "Валет";
        case 12:
            return "Дама";
        case 13:
            return "Король";
        case 14:
            return "Туз";
        default:
            return "Некорректный номер карты. Пожалуйста, введите число от 6 до 14.";
    }
}

const cardNumber = parseInt(prompt("Введите номер карты (6 - 14):"), 10);

if (!isNaN(cardNumber) && cardNumber >= 6 && cardNumber <= 14) {
    const cardRank = getCardRank(cardNumber);
    console.log(`Достоинство карты: ${cardRank}`);
} else {
    console.log("Пожалуйста, введите корректное число от 6 до 14.");
}