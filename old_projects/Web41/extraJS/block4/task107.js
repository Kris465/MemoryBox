const prompt = require('prompt-sync')();

function getDaysInMonth(monthNumber, isLeapYear) {
    if (monthNumber < 1 || monthNumber > 12) {
        return "Некорректный номер месяца. Пожалуйста, введите число от 1 до 12.";
    }

    switch (monthNumber) {
        case 1:
        case 3:
        case 5: 
        case 7: 
        case 8: 
        case 10: 
        case 12: 
            return 31;
        case 4: 
        case 6: 
        case 9: 
        case 11: 
            return 30;
        case 2: 
            return isLeapYear ? 29 : 28;
        default:
            return "Некорректный номер месяца.";
    }
}


const monthNumber = parseInt(prompt("Введите номер месяца (1-12):"), 10);


const isLeapYearInput = prompt("Является ли год високосным? (да/нет)").toLowerCase();
const isLeapYear = (isLeapYearInput === 'да');

const daysInMonth = getDaysInMonth(monthNumber, isLeapYear);


console.log(`Количество дней в месяце: ${daysInMonth}`);
alert(`Количество дней в месяце: ${daysInMonth}`);