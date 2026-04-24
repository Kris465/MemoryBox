const prompt = require('prompt-sync')();


function getMonthName(monthNumber) {
    const months = [
        "январь",
        "февраль",
        "март",
        "апрель",
        "май",
        "июнь",
        "июль",
        "август",
        "сентябрь",
        "октябрь",
        "ноябрь",
        "декабрь"
    ];

    if (monthNumber < 1 || monthNumber > 12) {
        return "Некорректный номер месяца. Пожалуйста, введите число от 1 до 12.";
    }

    return months[monthNumber - 1];
}

const monthNumber = parseInt(prompt("Введите номер месяца (1-12):"), 10);
const monthName = getMonthName(monthNumber);
console.log(`${monthName}`)