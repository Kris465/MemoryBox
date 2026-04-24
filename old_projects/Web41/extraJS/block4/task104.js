const prompt = require('prompt-sync')();

function getDayName(dayNumber) {
    let dayName;

    switch (dayNumber) {
        case 1:
            dayName = "Понедельник";
            break;
        case 2:
            dayName = "Вторник";
            break;
        case 3:
            dayName = "Среда";
            break;
        case 4:
            dayName = "Четверг";
            break;
        case 5:
            dayName = "Пятница";
            break;
        case 6:
            dayName = "Суббота";
            break;
        case 7:
            dayName = "Воскресенье";
            break;
        default:
            dayName = "Некорректный номер дня. Пожалуйста, введите число от 1 до 7.";
    }

    return dayName;
}

const dayNumber = 3; 
const result = getDayName(dayNumber);
console.log(result);