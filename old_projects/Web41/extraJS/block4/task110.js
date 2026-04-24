const prompt = require('prompt-sync')();

function getSuitName(m) {
    switch (m) {
        case 1:
            return "Пики";
        case 2:
            return "Трефы";
        case 3:
            return "Бубны";
        case 4:
            return "Червы";
        default:
            return null;
    }
}

function getRankName(k) {
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
            return null; 
    }
}
const suitNumber = parseInt(prompt("Введите номер масти (1 - Пики, 2 - Трефы, 3 - Бубны, 4 - Червы):"), 10);
const rankNumber = parseInt(prompt("Введите номер достоинства (6 - 14):"), 10);

const suitName = getSuitName(suitNumber);
const rankName = getRankName(rankNumber);

if (suitName && rankName) {
    console.log(`Полное название карты: ${rankName} ${suitName}`);
} else {
    console.log("Некорректный ввод. Пожалуйста, убедитесь, что номера масти и достоинства находятся в допустимых диапазонах.");
}