const prompt = require('prompt-sync')();

function getDayOfWeekWithStartDay(k, d) {
    const dayOfWeek = (k - 1 + d - 1) % 7; 
    switch (dayOfWeek) {
        case 0:
            return "Понедельник";
        case 1:
            return "Вторник";
        case 2:
            return "Среда";
        case 3:
            return "Четверг";
        case 4:
            return "Пятница";
        case 5:
            return "Суббота";
        case 6:
            return "Воскресенье";
    }
}

const k = parseInt(prompt("Введите номер дня (1 - 365):"), 10);
const d = parseInt(prompt("Введите номер дня недели для первого января (1 - Понедельник, ..., 7 - Воскресенье):"), 10);

if (k >= 1 && k <= 365 && d >= 1 && d <= 7) {
    console.log(`К-${k} день года: ${getDayOfWeekWithStartDay(k, d)}`);
} else {
    console.log("Некорректный ввод. Пожалуйста, введите число от 1 до 365 для дня и от 1 до 7 для дня недели.");
}